from openai import OpenAI


def generated_notes_from_images(client: OpenAI, image_base64: str, model: str="gpt-4o"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": """You are a great note taker, for the uploaded images, generate notes contains import information.
                        Output the information directly, do not say anything else.
                        If there are some tables, mind map, try to extract all orignial information from them with table or list.
                        Make it more like a note contains important information, not a description of the image.
                        A good structure of generated notes is like: 
                        <example-structure>
                        ## <-title->
                        <-summary->
                        <-details->
                        </example-structure>
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
    # return response
    # full_notes = ''
    # for chunk in response.choices:
    #     full_notes += chunk.choices[0].delta.get("content", "")
    #     yield full_notes
