import logging
from copy import deepcopy

import progressbar
from cv2 import cv2


class Plingo:
    def __init__(self, image_file_name=None):
        """Initialize the new program

        Args:
            image_file_name (str): Filename of the image to be loaded
        """

        self._set_command_index(0)
        self._input = None
        self._width = -1
        self._height = -1

        self._command_names = [x for x in self.__dir__() if x.startswith("_cmd_")]
        self._command_names = sorted(self._command_names)

        self._command_methods = [getattr(self, cmd) for cmd in self._command_names]

        if image_file_name:
            self._input_filename = image_file_name
            self._load_input()

    def _set_command_index(self, index):
        """Defines which of the three channels contains the command and which two others will contain the parameters.

        Args:
            index (integer): The index of the channel which contains the command
        """
        self._command_index = index % 3
        self._p1_index = (index + 1) % 3
        self._p2_index = (index + 2) % 3

    def _load_input(self):
        self._input = cv2.imread(
            self._input_filename,
        )
        self._input = cv2.cvtColor(self._input, cv2.COLOR_BGR2RGB)

        self._output = cv2.imread(self._input_filename)
        self._output = cv2.cvtColor(self._output, cv2.COLOR_BGR2RGB)

        logging.info("Loading input image")
        logging.debug(f"Loaded image: {self._input_filename}")
        logging.debug(f"Dimensions: {self._input.shape}")
        # TODO raise exception if third dimension is != 3

        self._height = self._input.shape[0]
        self._width = self._input.shape[1]
        # self._output = np.zeros((self._height, self._width, 4), np.uint8)

    def _call_command(self, cmd_number, p1, p2):
        cmd_number = cmd_number % len(self._command_names)

        try:
            # TODO better handling of output
            col = self._input[self._current_y][self._current_x]
            logging.info(
                f"{self._current_x:04d}/{self._current_y:04d} - ({col}): {self._command_names[cmd_number]}({p1:03d}, {p2:03d})"
            )

            method = self._command_methods[cmd_number]
            method(p1, p2)

        except Exception as e:
            logging.error(f"Error executing command `{cmd_number}({p1},{p2})`: {e}")

    def execute(self, show_progressbar=True, iterations=1):
        if show_progressbar:
            bar = progressbar.ProgressBar(
                max_value=(self._height * self._width * iterations)
            )

        for i in range(iterations):
            logging.info(f"Executing iteration {i:03d})")
            self._output = deepcopy(self._input)
            for self._current_y in range(self._height):
                for self._current_x in range(self._width):
                    # TODO take more control over output
                    cmd = self._input[self._current_y][self._current_x][
                        self._command_index
                    ]
                    p1 = self._input[self._current_y][self._current_x][self._p1_index]
                    p2 = self._input[self._current_y][self._current_x][self._p2_index]
                    self._call_command(cmd, p1, p2)
                    if show_progressbar:
                        bar.update(
                            (i * self._width * self._height)
                            + (self._current_y * self._width)
                            + self._current_x
                        )

            self._input = deepcopy(self._output)
            self._output = cv2.cvtColor(self._output, cv2.COLOR_RGB2BGR)

            iteration_text = ""
            if iterations > 1:
                iteration_text = str(i)
                iteration_text = iteration_text.zfill(len(str(iterations - 1)))
                iteration_text = f"_{iteration_text}"
            cv2.imwrite(f"{self._input_filename}_out{iteration_text}.png", self._output)

    def _cmd_000_noop(self, p1, p2):
        """Nothing will be done. The parameters will be ignored

        Args:
            p1 (integer): Ignored
            p2 (integer): Ignored
        """
        pass

    def _cmd_001_inc_command_pointer_pos(self, p1, p2):
        """Increase the index of the command channel.

        Args:
            p1: Ignored
            p2: Ignored
        """
        self._set_command_index(self._command_index + 1)

    def _cmd_002_dec_command_pointer_pos(self, p1, p2):
        """Decrease the index of the command channel.

        Args:
            p1: Ignored
            p2: Ignored
        """
        self._set_command_index(self._command_index - 1)

    def _cmd_003_invert(self, p1, p2):
        """Inverts the current pixel

        Args:
            p1: ignored
            p2: ignored
        """
        self._cmd_004_invert_plus_plus(0, 0)

    def _cmd_004_invert_plus_plus(self, p1, p2):
        """Invertes the pixel indicated by the offset

        Args:
            p1 (integer): Offset in positive X direction
            p2 (integer): Offset in positive Y direction
        """
        new_x = (self._current_x + p1) % self._width
        new_y = (self._current_y + p2) % self._height
        for i in range(3):
            self._output[new_y][new_x][i] = 255 - self._input[new_y][new_x][i]

    def _cmd_005_invert_plus_minus(self, p1, p2):
        self._cmd_004_invert_plus_plus(p1, -p2)

    def _cmd_006_invert_minus_plus(self, p1, p2):
        self._cmd_004_invert_plus_plus(-p1, p2)

    def _cmd_007_invert_minus_minus(self, p1, p2):
        self._cmd_004_invert_plus_plus(-p1, -p2)

    def _cmd_008_invert_channel(self, p1, p2):
        """Only invert a dedicated channel of the current pixel

        Args:
            p1 (integer): The channel to be inverted (channel = p1 % 3)
            p2: Ignored
        """
        i = p1 % 3
        self._output[self._current_y][self._current_x][i] = (
            255 - self._input[self._current_y][self._current_x][i]
        )

    def _cmd_009_copy_plus_plus(self, p1, p2):
        """Move the current pixel by the provided offset

        Args:
            p1 (integer): Offset in positive X direction
            p2 (integer): Offset in positive Y direction
        """
        new_x = (self._current_x + p1) % self._width
        new_y = (self._current_y + p2) % self._height
        self._output[new_y][new_x] = deepcopy(
            self._input[self._current_y][self._current_x]
        )
        logging.debug(
            f"  copied to {new_x:04d}/{new_y:04d} - {self._output[new_y][new_x]}"
        )

    def _cmd_010_copy_plus_minus(self, p1, p2):
        self._cmd_009_copy_plus_plus(p1, -p2)

    def _cmd_011_copy_minus_plus(self, p1, p2):
        self._cmd_009_copy_plus_plus(-p1, p2)

    def _cmd_012_copy_minus_minus(self, p1, p2):
        self._cmd_009_copy_plus_plus(-p1, -p2)

    def _cmd_013_switch_plus_plus(self, p1, p2):
        """Switches the current pixel with the one defined by the offset in p1 and p2

        Args:
            p1 (integer): Offset in positive X direction
            p2 (integer): Offset in positive Y direction
        """
        new_x = (self._current_x + p1) % self._width
        new_y = (self._current_y + p2) % self._height

        current_temp = deepcopy(self._input[self._current_y][self._current_x])
        other_temp = deepcopy(self._input[new_y][new_x])
        self._output[self._current_y][self._current_x] = other_temp
        self._output[new_y][new_x] = current_temp

    def _cmd_014_switch_plus_minus(self, p1, p2):
        self._cmd_013_switch_plus_plus(p1, -p2)

    def _cmd_015_switch_minus_plus(self, p1, p2):
        self._cmd_013_switch_plus_plus(p1, -p2)

    def _cmd_016_switch_minus_minus(self, p1, p2):
        self._cmd_013_switch_plus_plus(-p1, -p2)

    def _cmd_017_fade(self, p1, p2):
        """Mixes the current pixel with the 8 surrounding pixels

        Args:
            p1 (integer): Ignored
            p2 (integer): Ignored
        """
        counter = 0
        c = [0, 0, 0]
        for y in range(self._current_y - 1, self._current_y + 2):
            for x in range(self._current_x - 1, self._current_x + 2):
                if x >= 0 and x < self._width:
                    if y >= 0 and y < self._height:
                        counter += 1
                        logging.debug(
                            f"  adding {x:04d}/{y:04d} - ({self._input[y][x]})"
                        )
                        for i in range(3):
                            c[i] += self._input[y][x][i]

        for i in range(3):
            self._output[self._current_y][self._current_x][i] = round(c[i] / counter)
        logging.debug(
            f"  result           - ({self._output[self._current_y][self._current_x]})"
        )

    def _cmd_018_add_plus_plus(self, p1, p2):
        """Add the pixel indicated by the offset parameters to the current pixel.

        The value for each channel is clipped at 255

        Args:
            p1 (integer): The offset in positive X-direction
            p2 (integer): The offset in positive Y-direction
        """
        new_x = (self._current_x + p1) % self._width
        new_y = (self._current_y + p2) % self._height
        logging.debug(
            f"  adding {new_x:04d}/{new_y:04d} - ({self._input[new_y][new_x]})"
        )
        for i in range(3):
            v1 = int(self._input[self._current_y][self._current_x][i])
            v2 = int(self._input[new_y][new_x][i])
            self._output[self._current_y][self._current_x][i] = min(255, (v1 + v2))

    def _cmd_019_add_plus_minus(self, p1, p2):
        self._cmd_018_add_plus_plus(p1, -p2)

    def _cmd_020_add_minus_plus(self, p1, p2):
        self._cmd_018_add_plus_plus(-p1, p2)

    def _cmd_021_add_minus_minus(self, p1, p2):
        self._cmd_018_add_plus_plus(-p1, -p2)

    def _cmd_022_sub_plus_plus(self, p1, p2):
        """Subtract the pixel indicated by the offset parameters from the current pixel.

        The value for each channel is clipped at 255

        Args:
            p1 (integer): The offset in positive X-direction
            p2 (integer): The offset in positive Y-direction
        """
        new_x = (self._current_x + p1) % self._width
        new_y = (self._current_y + p2) % self._height
        logging.debug(
            f"  substracting {new_x:04d}/{new_y:04d} - ({self._input[new_y][new_x]})"
        )
        for i in range(3):
            v1 = int(self._input[self._current_y][self._current_x][i])
            v2 = int(self._input[new_y][new_x][i])
            self._output[self._current_y][self._current_x][i] = max(0, (v1 - v2))

    def _cmd_023_sub_plus_minus(self, p1, p2):
        self._cmd_022_sub_plus_plus(p1, -p2)

    def _cmd_024_sub_minus_plus(self, p1, p2):
        self._cmd_022_sub_plus_plus(-p1, p2)

    def _cmd_025_sub_minus_minus(self, p1, p2):
        self._cmd_022_sub_plus_plus(-p1, -p2)
