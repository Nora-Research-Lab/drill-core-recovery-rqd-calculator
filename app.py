import gradio as gr
from drill_core_recovery_rqd_calculator import calculate_recovery_rqd, create_rqd_gauge

def process_calculation(core_run_length, recovered_length, intact_pieces_length):
    try:
        # Validate inputs are positive numbers
        if core_run_length <= 0 or recovered_length < 0 or intact_pieces_length < 0:
            return "Error: All lengths must be positive values.", None
        
        result = calculate_recovery_rqd(core_run_length, recovered_length, intact_pieces_length)
        
        if isinstance(result, str):  # Error message
            return result, None
        
        core_recovery_pct, rqd_pct, rqd_class, recovery_class = result
        
        # Create the RQD gauge
        gauge_img = create_rqd_gauge(rqd_pct)
        
        output_text = f"""
Core Recovery Percentage: {core_recovery_pct:.1f}%
RQD Percentage: {rqd_pct:.1f}%
RQD Classification: {rqd_class}
Core Recovery Classification: {recovery_class}
        """.strip()
        
        return output_text, gauge_img
    
    except Exception as e:
        return f"An error occurred: {str(e)}", None

with gr.Blocks(title="Drill Core Recovery & RQD Calculator") as demo:
    gr.Markdown("# Drill Core Recovery & RQD Calculator")
    gr.Markdown("Enter the core drilling data to calculate recovery and RQD values.")
    
    with gr.Row():
        core_run_length = gr.Number(label="Core Run Length (m)", value=1.5)
        recovered_length = gr.Number(label="Recovered Core Length (m)", value=1.2)
        intact_pieces_length = gr.Number(label="Sum of Intact Pieces ≥ 0.10 m (m)", value=0.9)
    
    calculate_btn = gr.Button("Calculate")
    
    with gr.Column():
        output_text = gr.Textbox(label="Results", interactive=False, lines=4)
        gauge_output = gr.Image(label="RQD Gauge", type="filepath")

    calculate_btn.click(
        fn=process_calculation,
        inputs=[core_run_length, recovered_length, intact_pieces_length],
        outputs=[output_text, gauge_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
