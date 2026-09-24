import gradio as gr

from saline_aquifer_co2_storage_capacity_estimator import (
    estimate_capacity,
    format_capacity_html,
    format_category_html,
)


def calculate_capacity(area, thickness, porosity, density, efficiency):
    result = estimate_capacity(area, thickness, porosity, density, efficiency)
    return format_capacity_html(result), format_category_html(result)


with gr.Blocks(title="Saline Aquifer CO2 Storage Capacity Estimator") as demo:
    gr.Markdown(
        "# Saline Aquifer CO2 Storage Capacity Estimator\n"
        "Enter reservoir properties to obtain a screening-level estimate of saline aquifer CO2 storage capacity."
    )

    with gr.Row():
        with gr.Column():
            area_input = gr.Number(label="Area (km²)", value=100, precision=2)
            thickness_input = gr.Number(label="Net Thickness (m)", value=50, precision=2)
            porosity_input = gr.Slider(
                label="Porosity (fraction)",
                minimum=0.0,
                maximum=0.5,
                value=0.15,
                step=0.01,
            )
            density_input = gr.Number(
                label="CO2 Density at reservoir conditions (kg/m³)",
                value=700,
                precision=1,
            )
            efficiency_input = gr.Slider(
                label="Storage Efficiency Factor",
                minimum=0.01,
                maximum=0.10,
                value=0.04,
                step=0.001,
            )

        with gr.Column():
            calculate_button = gr.Button("Calculate", variant="primary")
            capacity_output = gr.HTML(value="Estimated CO2 storage capacity: —")
            category_output = gr.HTML(value="")

    gr.Markdown(
        "**Note:** This is a screening-level estimation. Typical input ranges: area > 0 km², "
        "net thickness > 0 m, porosity 0.0-0.5, CO2 density approximately 600-900 kg/m³, "
        "and storage efficiency 0.01-0.10."
    )

    calculate_button.click(
        fn=calculate_capacity,
        inputs=[area_input, thickness_input, porosity_input, density_input, efficiency_input],
        outputs=[capacity_output, category_output],
    )

    demo.load(
        fn=calculate_capacity,
        inputs=[area_input, thickness_input, porosity_input, density_input, efficiency_input],
        outputs=[capacity_output, category_output],
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
