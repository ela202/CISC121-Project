# CISC121-Project: Bubble Sort Visual Helper

## Demo Screenshot & Testing
I tested the app with lists of different variety, including, normal, already sorted, reverse sorted lists, and invalid inputs to verify the app's functionality.



## Why Bubble Sort?

I chose Bubble Sort because it is one that I have found confusing in the past, but through visual aids, I was able to understand the simplicity of this sorting algorithm. Its logic is very ideal for an educational app as it is easy to work through step by step, each pass has a pattern, and showcasing how the largest values "bubble" to end end is straight forward. My goal is to help beginners learn how Bubble Sort works through a clear and interactive visualization. 


## Problem Breakdown & Computational Thinking

### Decomposition
- Accept user input as a string seperated by commas
- Check and convert input into an integer list
- Run Bubble Sort alogithm utilizing nested loops
- Record every comparison and swap for visualization
- Output step-by-step procedure and final sorted list

### Pattern Recognition
- Bubble sort repeats the same pattern
- Compare two adjacent elements and swap if not in proper order
- Every pass moves the largest remaining element to the end ("bubbling")
- Inner loop shortens at every pass, and cn end early if there are no swaps

### Abstraction
- Users will only see an input box and simplified explanations of the comparisons, swaps, passes, and final result
- Technical details such as the loops, code, etc. will not be shown

### Algorithm Design
- Input: User will enter numbers seperated by commas
- Processing: Convert to list, apply Bubble Sort while following steps
- Output: Step-by-step breakdown of comparisons and swaps, and final sorted list

Input --> Check --> Convert to list --> Bubble Sort --> Output: Display steps + Sorted List


## Steps to Run
1. Clone this Github repository
2. Install dependencies (bash): pip install -r requirements.txt
3. Run the app: python app.py


## Hugging Face Link
https://huggingface.co/spaces/ela-art/CISC-Project 

## Author & Acknowledgment
Author: Ela Aydiner

Acknowledgements: CISC-121 course content, Gradio documentation, Hugging Face
