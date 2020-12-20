## 000 - noop 

Nothing will be done. The parameters will be ignored

        Args:
            p1 (integer): Ignored
            p2 (integer): Ignored
         

## 001 - inc_command_pointer_pos 

Increase the index of the command channel.

        Args:
            p1: Ignored
            p2: Ignored
         

## 002 - dec_command_pointer_pos 

Decrease the index of the command channel.

        Args:
            p1: Ignored
            p2: Ignored
         

## 003 - invert 

Inverts the current pixel

        Args:
            p1: ignored
            p2: ignored
         

## 004 - invert_plus_plus 

Invertes the pixel indicated by the offset

        Args:
            p1 (integer): Offset in positive X direction
            p2 (integer): Offset in positive Y direction
         

## 005 - invert_plus_minus 

_not yet documented_ 

## 006 - invert_minus_plus 

_not yet documented_ 

## 007 - invert_minus_minus 

_not yet documented_ 

## 008 - invert_channel 

Only invert a dedicated channel of the current pixel

        Args:
            p1 (integer): The channel to be inverted (channel = p1 % 3)
            p2: Ignored
         

## 009 - copy_plus_plus 

Move the current pixel by the provided offset

        Args:
            p1 (integer): Offset in positive X direction
            p2 (integer): Offset in positive Y direction
         

## 010 - copy_plus_minus 

_not yet documented_ 

## 011 - copy_minus_plus 

_not yet documented_ 

## 012 - copy_minus_minus 

_not yet documented_ 

## 013 - switch_plus_plus 

Switches the current pixel with the one defined by the offset in p1 and p2

        Args:
            p1 (integer): Offset in positive X direction
            p2 (integer): Offset in positive Y direction
         

## 014 - switch_plus_minus 

_not yet documented_ 

## 015 - switch_minus_plus 

_not yet documented_ 

## 016 - switch_minus_minus 

_not yet documented_ 

## 017 - fade 

Mixes the current pixel with the 8 surrounding pixels

        Args:
            p1 (integer): Ignored
            p2 (integer): Ignored
         

## 018 - add_plus_plus 

Add the pixel indicated by the offset parameters to the current pixel.

        The value for each channel is clipped at 255

        Args:
            p1 (integer): The offset in positive X-direction
            p2 (integer): The offset in positive Y-direction
         

## 019 - add_plus_minus 

_not yet documented_ 

## 020 - add_minus_plus 

_not yet documented_ 

## 021 - add_minus_minus 

_not yet documented_ 

## 022 - sub_plus_plus 

Subtract the pixel indicated by the offset parameters from the current pixel.

        The value for each channel is clipped at 255

        Args:
            p1 (integer): The offset in positive X-direction
            p2 (integer): The offset in positive Y-direction
         

## 023 - sub_plus_minus 

_not yet documented_ 

## 024 - sub_minus_plus 

_not yet documented_ 

## 025 - sub_minus_minus 

_not yet documented_ 


