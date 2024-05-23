def create_notion_page(token, database_id, content):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # Create a new page with the markdown content
    data = {
        "parent": { "database_id": database_id },
        "properties": {
            "title": [
                {
                    "text": {
                        "content": "Markdown Content"
                    }
                }
            ]
        },
        "children": [
            # {
            #     "object": "block",
            #     "type": "image",
            #     "image": {
            #         "type": "external",
            #         "external": {
            #             "url": image_url
            #         }
            #     }
            # },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": content
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Page created successfully!")
    else:
        print(f"Failed to create page: {response.status_code} - {response.text}")
