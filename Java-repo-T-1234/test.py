import json
import os
import time
from typing import Dict, Any, Optional

from anthropic import AnthropicVertex
from flask import jsonify

import config
from models import project_summary_db, code_profile_db

def get_validated_service_ai_response(system_prompt: str, user_content: str) -> Dict[str, Any]:
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            if not system_prompt:
                print("System prompt is missing.")
                return {"error_code": 400, "message": "System prompt is missing."}
            
            start_time = time.time()
            LOCATION = "us-east5"
            client = AnthropicVertex(region=LOCATION, project_id=config.LLM_PROJECT_ID)

            code_history = [{"role": "user", "content": user_content}]
            
            try:
                message = client.messages.create(
                    temperature=0,
                    top_k=0,
                    top_p=0,
                    max_tokens=4096,
                    system=system_prompt,
                    model="claude-3-5-sonnet@20240620",
                    messages=code_history
                )
            except Exception as e:
                print(f"Error communicating with AI service: {e}")
                return {"error_code": 502, "message": "Failed to communicate with AI service."}

            ai_answer = message.content[-1].text
            # print(f"\nTime taken for query analysis request: {time.time() - start_time} s")
            # print("Response from Bypassing method: ", ai_answer)

            json_extracted = ai_answer
            json_code_start = "