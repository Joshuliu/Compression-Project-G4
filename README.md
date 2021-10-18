# Group Project 1: Compression 
###### Joshua, Lauren, Dylan, Ud 
### M012 Group 4 

## Organization of Characters 
- 72 total characters 
- Long Characters 
  - 6 bits total (2<sup>6</sup> = 64) 
  - Starts with 1 
  - Characters (organized as capital, lowercase, special, phrases) 
    - Capital (26) : A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z 
      - Will always start with 11 
    - Lowercase (18): b, c, d, f, g, j, k, l, m, p, q, r, u, v, w, x, y, z 
      - Will always start with 10 
    - Phrases (12): th  er  an  on   and    the  to   you  of  be  in 
      - Will always start with 11 
      - Note the spaces around some phrases indicated by highlights 
    - Special (8):  .   ,   -   !   '   "   \n    
      - Can start with either 10 or 11 (uses remaining bits) 
      - <space> indicated as a highlighted space 
    - Excluding the first character (always 1, used to indicate long char) and the second character (used to indicate capital, lowercase, phrase, or special char), long characters follow a standard pattern going down the list of 0000, 0001, 0010, 0011, 0100, etc. 
- Short Characters  
  - 3 bits total (2<sup>3</sup> = 8) 
  - Starts with 0 
  - Characters:  
    - e, t, a, i, o, n, s, h 
  - Excluding the first character (always 0, used to indicate short char), Short characters follow a standard pattern going down the list by 0000, 0001, 0010, 0011, 0100, etc. 
## List of Binary Representation of Characters
|Character |Binary |
| - | - |
|A |1100000 |
|B |1100001 |
|C |1100010 |
|D |1100011 |
|E |1100100 |
|F |1100101 |
|G |1100110 |
|H |1100111 |
|I |1101000 |
|J |1101001 |
|K |1101010 |
|L |1101011 |
|M |1101100 |
|N |1101101 |
|O |1101110 |
|P |1101111 |
|Q |1110000 |
|R |1110001 |
|S |1110010 |
|T |1110011 |
|U |1110100 |
|V |1110101 |
|W |1110110 |
|X |1110111 |
|Y |1111000 |
|Z |1111001 |
|a  |0000 |
|b  |1000000 |
|c  |1000001 |
|d  |1000010 |
|e  |0001 |
|f  |1000011 |
|g |1000100 |
|h  |0010 |
|i  |0011 |
|j |1000101 |
|k |1000110 |
|l |1000111 |
|m |1001000 |
|n |0100 |
|o |0101 |
|p |1001001 |
|q |1001010 |
|r |1001011 |
|s |0110 |
|t |0111 |
|u |1001100 |
|v |1001101 |
|w |1001110 |
| - | - |
|x |1001111 |
|y |1010000 |
|z |1010001 |
|.|101111 |
|, |1111011 |
|- |1111100 |
|! |1111101 |
|" |1111110 |
|' |1111111 |
|\n |1010010 |
|` `|1010011 |
|th |1010100 |
|er |1010101 |
|an |1010110 |
|on |1010111 |
|` and ` |1011000 |
|` the` |1011001 |
|to |1011010 |
|` you` |1011011 |
|of |1011100 |
|be |1011101 |
|in |1011110 |
|is |1011111 |

