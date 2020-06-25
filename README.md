# Python-Scripts
Various random bits of code, all written in Python, doing various often small and always useless things. Really, the only reason I'm saving these is on the off chance that a giant Github Repo full of Python scripts somehow comes in handy in the future. More to come in the vaguely defined future, I'm sure.

Man, having these hosted in Github makes me feel like I have to be all professional and stuff.

Uh, [here.](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

---

## [Primes](/primes.py)

Generates an arbitrary amount of prime numbers using a method vaguely related to [prime sieves](https://en.wikipedia.org/wiki/Generation_of_primes#Prime_Sieves).

Start with a list of primes containing 2, then for every other number from 3 until a specified maximum number, test each number to see if it is divisible by any of the primes smaller than it's square root.<sup>[1](#footnote1)</sup> If not, the number is added to the primes list.

Also has some auxillary code to see how much time and memory the prime generation has taken, frankly just because I was curious at the time.

<sup><a name="footnote1">1</a>: We only need to go up to the square root because of the [Fundamental Theorem of Arithmatic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic), which is a damn good name for a thing, might I add.</sup>


## [Touch Tone Letters](touchToneLetters.py)

Takes in a string that represents how text was entered into older keypad phones, like one of [these](https://en.wikipedia.org/wiki/Telephone_keypad#/media/File:Telephone-keypad2.svg), and converts it to plaintext. For example, `33-22-444-444-555 9-555-666-444-5` becomes `hello world`.

Not actually very complex at all, and relies a bit too much on the input being properly-enough formatted, but I whipped this up because of a meme I saw so whatever. Takes the input string, cleans it a bit, and divides it by spaces. Each chunk is checked for the first integer and the length, and those two values are compared against a 2d array to find the appropriate letter, which it adds to a return string.

## [Words](words.py)

Does a bunch of random stuff with a [list of words](/words.txt), sourced from [dwyl's repo here](https://github.com/dwyl/english-words). To be honest, there isn't *too* much to this one at all, just a few sorts and direct comparisons to lists. I just like typing long words quickly, and finding words where each letter alternates between sides on the keyboard is a great way to do so.
