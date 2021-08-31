# Description
What integer does this program print with arguments 3854998744 and 915131509? File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

# Understanding the basics
This my first experience with assembly so I must say it has been quite challenging
```arm
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
```
So here we go. `sp` stands for the stack pointer, and the `sub` instruction is a substraction with three components:
```arm
sub x,y, #z
```
Substract `#z` (# denotes a constant value) fro `y` and store it in `x`. Why is this instruction even here? It makes space on the stack for variables, and since we have two, substracting `16` should be just enough. In the next two lines we have some essential instructions:
```arm
str	w0, [sp, 12]
str	w1, [sp, 8]
```
`str` stands for `store`, and `w0` and `w1` are the user input variables. So we `store` the values in `w0` and `w1`  on the stack (`sp`). The number denotes the offset on the stack. So `str	w0, [sp, 12]` means `store w0 on the stack at offset 12`. Pretty neat.
```arm
ldr	w1, [sp, 12]
ldr	w0, [sp, 8]
```
Here we load the values from the stack at a given offset into a variable. So `load the value at offset 12 on the stack into w1` is equal to `ldr w1, [sp, 12]`. Also neat! And very important.
```arm
cmp	w1, w0
```
Compare the values by substracting `w0` from `w1`. So basically a `sub` except that we do not store the value. Next!
```arm
bls .L2
```
Right, this is a `branch if less` instruction, if `w0` is smaller than `w1` `branch` or `jl` (for the x86 guys) to `.L2`. And at the end load a value again and `b` (simple branch `jmp` in x86). Very nice!

# Remaining functions

```arm
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
```
At `.L2` we load a value from the `stack at offset 8` into the variable w0 and continue execution back in `func1`. In `.L3` we just `add` 16 back to `sp`, ie. we fill the stack back again.

# Main

```arm
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16] # 4134207980
	str	w0, [x29, 44] # 950176538
	str	x1, [x29, 32]
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi
	mov	w1, w0        # w1 -> 950176538
	mov	w0, w19       # w0 -> 4134207980
	bl	func
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
```
Here is the main function with my added "comments". So if we add everything together, what happens? If we just skip to the important bit, before branching to `.L3` the value from `[sp, 12]` is loaded and printed! So what is the flag?
```E5C69CD8z
picoCTF{E5C69CD8}
```
Convert `4134207980` into a 32 bit hex string and that is it.