import openai
openai.api_key = "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"
def send_req(transcribed_text=""):
    if transcribed_text == "":
        return False;
    print("Sending request to GPT-3");
    # Parameters for OpenAI GPT-3 API
    model_engine = "text-davinci-002"
    temperature = 0.5
    max_tokens = 300
    
    prompt="What is the emergency type, location, and priority of the following message. Your response must be in the following JSON format: {name, location, emergency_type, priority, reply_msg}. Available emergency_types=['Ambulance', 'NSG', 'Police', 'Rescue team', 'Fire brigade', 'Forest ranger']. Available priority=['high', 'medium', 'low']. Prompt: "+transcribed_text;

     
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    return (response["choices"][0]["text"])

# Path: server\gpt.py