from openai import OpenAI


def generated_notes_from_images(client: OpenAI, image_base64: str, model: str="gpt-4o"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": """You are a great note taker, for the uploaded images, generate notes contains import information.
                        The images usually taken from slides, meeting notes, what you need to do is help to take notes from the images.
                        Output the information directly, do not say anything else.
                        Make it more like a note contains important information, not a description of the image.
                        A good structure of generated notes is like: 
                        <example-structure>
                        ## <-title->
                        <-a paragraph of summary->
                        <-details information from the image->
                        </example-structure>
                        If there are some tables, try to extract all orignial information in table format.
                    """},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        },
                    },
                ],
            },
        ], stream=True)
    notes = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            notes = chunk.choices[0].delta.content
        yield notes
