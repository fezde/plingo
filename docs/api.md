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

_not yet documented_ 

## 004 - invert_channel 

Only invert a dedicated channel

        Args:
            p1 (integer): The channel to be inverted (channel = p1 % 3)
            p2: Ignored
         

## 005 - copy_plus_plus 

Move the current pixel by the provided offset

        Args:
            p1 (integer): Offset in positive X direction
            p2 (integer): Offset in positive Y direction
         

## 006 - copy_plus_minus 

_not yet documented_ 

## 007 - copy_minus_plus 

_not yet documented_ 

## 008 - copy_minus_minus 

_not yet documented_ 

## 009 - switch_plus_plus 

Switches the current pixel with the one defined by the offset in p1 and p2

        Args:
            p1 (integer): Offset in positive X direction
            p2 (integer): Offset in positive Y direction
         

## 010 - switch_plus_minus 

_not yet documented_ 

## 011 - switch_minus_plus 

_not yet documented_ 

## 012 - switch_minus_minus 

_not yet documented_ 

## 013 - fade 

Mixes the current pixel with the 8 surrounding pixels

        Args:
            p1 (integer): Ignored
            p2 (integer): Ignored
         

## 014 - add_plus_plus 

Add the pixel indicated by the offset parameters to the current pixel.

        The value for each channel is clipped at 255

        Args:
            p1 (integer): The offset in positive X-direction
            p2 (integer): The offset in positive Y-direction
         

## 015 - add_plus_minus 

_not yet documented_ 

## 016 - add_minus_plus 

_not yet documented_ 

## 017 - add_minus_minus 

_not yet documented_ 

## 018 - sub_plus_plus 

Subtract the pixel indicated by the offset parameters from the current pixel.

        The value for each channel is clipped at 255

        Args:
            p1 (integer): The offset in positive X-direction
            p2 (integer): The offset in positive Y-direction
         

## 019 - sub_plus_minus 

_not yet documented_ 

## 020 - sub_minus_plus 

_not yet documented_ 

## 021 - sub_minus_minus 

_not yet documented_ 


