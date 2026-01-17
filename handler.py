import runpod
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model at startup
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    "YuanLabAI/Yuan3.0-Flash",
    trust_remote_code=True,
    device_map="auto" 
)
tokenizer = AutoTokenizer.from_pretrained(
    "YuanLabAI/Yuan3.0-Flash",
    trust_remote_code=True
)
print("Model loaded.")

def handler(event):
    input_data = event['input']
    prompt = input_data.get('prompt')
    
    if not prompt:
        return {"error": "No prompt provided"}

    # Run inference
    inputs = tokenizer(prompt, return_tensors="pt")
    if hasattr(model, "device"):
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        
    outputs = model.generate(**inputs, max_new_tokens=100)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return {"output": result}

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
