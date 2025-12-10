# CISC121-Project: Bubble Sort Visual Helper

## Demo Screenshot & Testing
I tested the app with lists of different varieties, including normal, already sorted, reverse sorted lists, and invalid inputs, to verify the app's functionality.

### Demo Userface Screenshot in Hugging Face

<img width="1906" height="764" alt="image" src="https://github.com/user-attachments/assets/95e490de-a0e6-47f0-a73c-67e8a9589779" />

### Normal unsorted list
Input: 5, 1, 4, 7, 2
Output: Sorted list: [1, 2, 4, 5, 7]

<img width="363" height="730" alt="image" src="https://github.com/user-attachments/assets/4e0e2ab2-2cf4-4f19-ac24-e4c9b57919c2" />

### Already sorted list
Input: 1, 2, 3, 4
Output: Sorted list: [1, 2, 3, 4]
Showcasing that algorithm stops early after a pass with no swaps.

<img width="347" height="634" alt="image" src="https://github.com/user-attachments/assets/d8716257-3215-4055-9e04-31270eb95793" />

### Reverse sorted list
Input: 9, 7, 6, 2, 1
Output: Sorted list: [1, 2, 6, 7, 9] 
<img width="311" height="727" alt="image" src="https://github.com/user-attachments/assets/ce43d662-df6d-4800-b03f-9cd4da3fa28e" />

### List with duplicates
Input: 9, 9, 4, 1
Output: Sorted list: [1, 4, 9, 9]

<img width="263" height="653" alt="image" src="https://github.com/user-attachments/assets/8c41f938-40af-42ea-9db0-b3fb3d390829" />

Negative and positive numbers
Input: 0, -2, 8, -1
Output: Sorted list: [-2, -1, 0, 5]

<img width="315" height="686" alt="image" src="https://github.com/user-attachments/assets/05878339-0fc4-4cae-9c75-2aa8ec37e4cd" />


## Why Bubble Sort?

I chose Bubble Sort because it has been confusing for me in the past, but with visual aids, I was able to understand its simplicity. Its logic is very ideal for an educational app as it is easy to work through step by step, each pass has a pattern, and showcasing how the largest values "bubble" to the end is straightforward. My goal is to help beginners learn how Bubble Sort works through a clear and interactive visualization. 


## Problem Breakdown & Computational Thinking

### Decomposition
- Accept user input as a string separated by commas
- Check and convert input into an integer list
- Run the Bubble Sort algorithm utilizing nested loops
- Record every comparison and swap for visualization
- Output step-by-step procedure and final sorted list

### Pattern Recognition
- Bubble sort repeats the same pattern
- Compare two adjacent elements and swap if not in proper order
- Every pass moves the largest remaining element to the end ("bubbling")
- Inner loop shortens at every pass, and can end early if there are no swaps

### Abstraction
- Users will only see an input box and simplified explanations of the comparisons, swaps, passes, and final result
- Technical details such as the loops, code, etc., will not be shown

### Algorithm Design
- Input: User will enter numbers separated by commas
- Processing: Convert to list, apply Bubble Sort while following steps
- Output: Step-by-step breakdown of comparisons and swaps, and final sorted list

Input --> Check --> Convert to list --> Bubble Sort --> Output: Display steps + Sorted List

## Steps to Run
1. Clone this GitHub repository
2. Install dependencies (bash): pip install -r requirements.txt
3. Run the app: python app.py

## Hugging Face Link
https://huggingface.co/spaces/ela-art/CISC-Project 

## Author & Acknowledgment
Author: Ela Aydiner
Acknowledgements: CISC-121 course content, Gradio documentation, Hugging Face
