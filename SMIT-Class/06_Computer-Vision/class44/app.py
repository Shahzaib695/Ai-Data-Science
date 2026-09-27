from ultralytics import YOLO
import gradio as gr

model = YOLO('best_licence_model.pt')
def pred_img(img):
    img = model.predict(img)
    return img[0].plot()
app = gr.Interface(fn=pred_img, inputs='image', outputs='image')
app.launch(share=True)
