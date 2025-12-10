import gradio as gr

def bubble_sort(arr):
    log = []
    n = len(arr)

    # For recording steps
    log.append(f"Initial list: {arr}")

    for p in range(n - 1):
        swap = False

        for i in range(n - 1 - p):

            log.append(f"Compare {arr[i]} and {arr[i+1]}")

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
                log.append(f"  → Swapped → {arr}")
            else:
                log.append(f"  → No swap → {arr}")

        log.append(f"End of pass {p + 1}: {arr}")

        if not swap:
            log.append("No swaps in this pass → List sorted early.")
            break

    log.append(f"Final sorted list: {arr}")
    return log, arr


# Function that Gradio will call when the user clicks the button
def run_bubble_sort(user_input):
    # Checks for empty input
    if user_input.strip() == "":
        return "Please enter numbers separated by commas.", ""

    # Converts input into a list of integers
    try:
        nums = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
    except ValueError:
        return "Invalid input. Make sure all values are integers.", ""

    # Checks if list is empty after
    if len(nums) == 0:
        return "Please enter at least one number.", ""

    # Run bubble sort with step tracking
    steps, sorted_list = bubble_sort(nums)

    # Formats result for Gradio outputs
    steps_text = "\n".join(steps)
    final_text = f"Sorted list: {sorted_list}"

    return steps_text, final_text


# Gradio Interface
with gr.Blocks(title="Bubble Sort Visual Helper 🫧") as demo:

    gr.Markdown("# 🫧 Bubble Sort Visual Helper 🫧")
    gr.Markdown(
        "Enter numbers separated by commas (e.g., `5, 1, 4, 2`). "
        "This app will show Bubble Sort step by step."
    )

    input_box = gr.Textbox(
        label="Input List",
        placeholder="Example: 5, 1, 4, 2, 8"
    )

    sort_button = gr.Button("Run Bubble Sort")

    steps_output = gr.Textbox(
        label="Step-by-Step Explanation",
        lines=15
    )

    final_output = gr.Textbox(
        label="Final Sorted List"
    )

    sort_button.click(
        fn=run_bubble_sort,
        inputs=input_box,
        outputs=[steps_output, final_output]
    )


if __name__ == "__main__":
    demo.launch()
