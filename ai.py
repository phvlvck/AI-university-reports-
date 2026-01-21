import requests
import json

url = "https://chat.qwen.ai/api/v2/chat/completions"

params = {
    'chat_id': "5b27388a-c96d-4da4-b1b2-cc22064125b1"
}

payload = {
    "stream": True,
    "version": "2.1",
    "incremental_output": True,
    "chat_id": "5b27388a-c96d-4da4-b1b2-cc22064125b1",
    "chat_mode": "normal",
    "model": "qwen3-max-2025-09-23",
    "parent_id": "835f374f-132f-4ebb-b6a3-4af60046c246",
    "messages": [
        {
            "fid": "b0ab2f1d-a681-4de8-a345-60b64ccce72a",
            "parentId": "835f374f-132f-4ebb-b6a3-4af60046c246",
            "childrenIds": [
                "ae67c7fe-6a46-4f90-b91b-1c6592d4db20"
            ],
            "role": "user",
            "content": """أنت خبير أكاديمي محترف. أنتج تقريراً جامعياً باللغة العربية.
                المتطلبات:
                1. introduction: نص طويل مفصل.
                2. sections: مصفوفة تحتوي على كائنات {title: string, content: string}. يجب توفير أقسام كافية لملء عدد الصفحات المطلوب.
                3. conclusion: نص خاتمة رصين.
                4. references: مصفوفة نصوص للمراجع.
اصنع لي تقرير عن الذبحه الصدريه في الطب""",
            "user_action": "chat",
            "files": [],
            "timestamp": 1769014602,
            "models": [
                "qwen3-max-2025-09-23"
            ],
            "chat_type": "t2t",
            "feature_config": {
                "thinking_enabled": False,
                "output_schema": "phase",
                "research_mode": "normal"
            },
            "extra": {
                "meta": {
                    "subChatType": "t2t"
                }
            },
            "sub_chat_type": "t2t",
            "parent_id": "835f374f-132f-4ebb-b6a3-4af60046c246"
        }
    ],
    "timestamp": 1769014602
}

headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
    'Accept': "application/json",
    'Content-Type': "application/json",
    'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    'Version': "0.1.34",
    'bx-umidtoken': "T2gAEHq4_Xqn6RzSOSs7hk1xqWRPu4J_PzSh0CmXQ3m-lfLXtDeHylN7LET_K9o_YrM=",
    'Accept-Language': "en-US,en;q=0.9",
    'source': "h5",
    'bx-ua': "231!wwD31+mUW3E+joX4f43l190jUq/YvqY2leOxacSC80vTPuB9lMZY9mRWFzrwLE2ZjAyWofypQA+/eUi1ddzRGDSBWSi7R5PNCCAweSTVdZQwXhQ+bXCtuyFn1ktcMkrzFVeI78WTrdkaJxjkk3F/6ApUx+rnxuCQfXX6UmerV1ZoAuD67VPYmBEDhve5f6aAXxOn6jd50Z0O/N84icvR1Q6qo9hLDkSr+/mepk4qk4MsH6okTUsv0gNqS++++4mWIA+W6vB3+3RTkijOgR3jY0A4+mBu+yUHqi+C68G+QXgU61AA9HpnqCz++Ie0+4m4je++Btzj+KFU+heO9NBjfg/+WUTc+4mUY1Sk63zJ+DI0Djj09AjTNCF/+yDc+wrPqi++68zm+KgU3DoUjOokjPBDj+IjQEnla8U4yYzsW8FTcs4ZfcguIWXKp3gD2/XT+lL4CHNzn4jvKVAN6YhboQLLuTTi+PNTNVsTCMMo4qlOPciWmRjrtxh1gT2bPTagK3ahr1jjjofDJHkc1jAJ+gNDvzRGJqHuQs800ZbJlSjRP69zwRZMLzTRFW59Y3lC+wL1XCsLnEpwA+6Nm2RpMJcZ8aWpP4GyOMif9UOS4bEsvrCS4TvxPhAp8fcwD8sMJ3s+lbhYkLtsSWNCe0r5LqrMvAPGbb1LwIK7KV1HSmp+S0Fw6ST6PI2HayKvuC87fdpWJ1QsxuIkt+IC/WV5S0kc/9GDbucwfxRNq01TVni9w8qcnVSY7Q84PB+WwELZRruSr/ccsBeFwpfve0tUEcUs6NVfiosiUFb10Y0J0c44IUgXhtMl5ErS25/MoNKjAX/l5nqRC67dlLwF0JuEMb2a8rLwXDv9RdZn/7zk/jfcgMSZ1S08977NXK0W6CrTb9qTxLtnqSLO+HnyxQdah3Vk5eIakssS9ljR8cWhYv+PVosccqynAnFI7UsEUzHET1kQ8O07MZ5POQZocD2/dtHXLie8tniKEDq8kZ85Vm726VYGVWXka55ISKCG3wH6Ajz/5uH0f/tz1qvtbkeSkSP4mi6qSTuEriUJnMaTGbrruomC9nuWkE7NlLB5sqWFlucTVVnoi5qxf+cY7yooG2VHqigHTpI80MSS8eeKR1/mUh2Lk5rL+7DWn/B9BAvWXPkrBu9mqOVhUCpxvBKfC/YktWcdxsBcKUQNesjl2bMmFa0GwxFmwonyASG6vuf2tfpvIgTwVQyEeUvsiBPuE90QRME6yNfaWlhg3ErL3TIx9TBayWzl6CiuDwG6+WKM8buXFf4WTPw/9emQ5RV9v54Vxal3PmjxKYJJ4rZxAI5ZvFQswTIYab3tEOBEqcJKi3cRybQKwLVaC+qgKA24jygJujymcBv9HJssrTkgmaiQvOnoOEDcI+g/Lb0/J5tV7oAYH+xj+INMHrUkJ+zU45ZK2JHzsSRhYYG3SmWqN3EXE5ZjS1B10ow2IYHcTaYAw9dl+IJEbv9uTVGt20IFJY6W7PmYQkMt5SASEQ9wqX5gimRjnsM8y6hDLS4l2+9YYtItNaY7/ErwiTZRKUVaJHPsEFeBbM8czOfVU52vkPG36B1fh7s2jHjTXc4Llmkl5xGB1bgAhPK3AwN0UWFuSh5tMEtUvJ4DpMAV1IVXCx15ZLZG",
    'sec-ch-ua-mobile': "?1",
    'bx-v': "2.5.36",
    'Timezone': "Wed Jan 21 2026 19:56:42 GMT+0300",
    'X-Accel-Buffering': "no",
    'X-Request-Id': "06aa11ef-e48c-4bc5-8e57-692609b0d2c3",
    'sec-ch-ua-platform': "\"Android\"",
    'Origin': "https://chat.qwen.ai",
    'Sec-Fetch-Site': "same-origin",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Dest': "empty",
    'Referer': "https://chat.qwen.ai/c/5b27388a-c96d-4da4-b1b2-cc22064125b1",
    'Cookie': "_gcl_aw=GCL.1769005592.CjwKCAiAj8LLBhAkEiwAJjbY72j4l-rF4-NtvHhlEDA-4g8R77I7Yv0DyTGeuHhV2Kf1A2ha3UNNVRoC-vYQAvD_BwE; _gcl_gs=2.1.k1$i1769005589$u64539133; _gcl_au=1.1.1903109747.1769005592; _bl_uid=zLmadkh0o1U47b9sm8Ia9pRk1Ime; cna=HND3IaP6LlQCAangQfPwDK3F; xlly_s=1; acw_tc=0a03e59417690133407585283e2a5f5e57058308c3aaf2e23358d6b0f3cb57; x-ap=ap-southeast-1; sca=78135166; cnaui=51e58a4b-722d-457a-a522-dedb3e1f9566; aui=51e58a4b-722d-457a-a522-dedb3e1f9566; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUxZTU4YTRiLTcyMmQtNDU3YS1hNTIyLWRlZGIzZTFmOTU2NiIsImxhc3RfcGFzc3dvcmRfY2hhbmdlIjoxNzY5MDEzNTg2LCJleHAiOjE3Njk2MTg0NTl9.wKZPS5HTwtW6GZbCGI8VVUZAiGOqy7f_lQ2sY0qT2GA; atpsida=09ce29460eae5a124d7e433b_1769013674_12; tfstk=gq2i8qvv3AAQFMTFEEk1_EcAuZCp6AMjfrpxkx3VT2uQBrCskWD44zcxg1NT-q0Eqii2QV-eYr33BhoVlJmUPrvq_sGZiXuLlRnqgxREYmnv_iGanW90VowOfxIsClMj3aQRe-q_fxaJo-czI2RE2kJwbK5KLysMzN7ReTEaJVD-1aFt6d1I0mkqbjJq8Mmmmmkq_m8Fxmov7IJaukSnRmLq0doVL9or2dkq3rkeY2iq3qzq_MqERmkqunDViVwgBJ7vbRnNSjpT4ccizlugzowEhUnUbVvwokiisCEZ-KJ4dSzMergcLU0bLrDrsW_H1uDZ5zm8W9Jgrly_S7zVop0raWhYIfWHplGuw7l3hT9sQP3tBRHPFFuY9u2mm-_fKzqaCPVc4BdeaN59h4B3DIOj_DinysvrMRh8GxvGxMAzBfoIYwshxIOj_DinyMjHMYcZAD7C.; isg=BImJ8lLkBElSMPi8ebRex28FmLfj1n0Iy59g9Sv-P3CacrGEZCfg2fnksYjiYBVA; ssxmod_itna=1-QqjxgDniDtiQ0=d4YjIxYKAQDQDuKDRC1rDBP01OHDuxiK08D6D4BRD1qi=6pi5k=3mdyDe=3Z0iNDlELneDRPqibD_fWjKd9W82GKeRh7iTioNt0DgPNYvIl7edyQsgMpjuOHZRBcgfeDQxi8DBKDcxDzDDbWDnKD9giHpDiiDBeD5PYDP6YDAWoDbxiTD0R_mtxDj=7QObGtE40ieG3DNxDCOWBIdRoDT6B=GDi3dpoDXpQDv68KdtahDQK=Gt3EPH4YR21oCxR4sNHNKliqkD4xkQgqwg0qgl0qZj1ZCr8Nny0rG0prIiO=MOrw8nGbFBNVEeqBxfkqgGxoE5_u5KDY3Y1IkDpY5K0DeDxtQ5GAwkuD4D; ssxmod_itna2=1-QqjxgDniDtiQ0=d4YjIxYKAQDQDuKDRC1rDBP01OHDuxiK08D6D4BRD1qi=6pi5k=3mdyDe=3Z0ioD=a4xAPY3x1xGailD2aAYD0yGf2871iwUe4q3Hao1kmUSDq1ye/ZGxULFX7yOkfd_fQAx4DOwlI2ti_MxV7WQ/l3K0_hjeLlhBIjRc0MrBSdffnrLKGY5VzD=PuOUS_x=4ukxqUf34mSo4tS62zwHKN=XS8Den3f3cWiNwrFdgAqHL3nFzobNKYZGfFa8ciwDzOddZD5y2NpGXH034Fp=z=M=f0PzXgdyBQ0fCzD4ZWDA2Nbx_bDmi7G=BIqrvK0jhr5zgpTgPGCDyWY59GPzfW6xqDPGm3wZ259rD4eqQvT6iGBK5xeYRrv7_GBmzjGzj3P/i4jxi7G5QGqFn59w=BexD"
}

try:
    response = requests.post(url, params=params, data=json.dumps(payload), headers=headers, stream=True)
    
    if response.status_code == 200:
        full_response = ""
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                
                # تخطي الأسطر الفارغة
                if line_str.strip() == "":
                    continue
                    
                # التحقق مما إذا كان السطر يحتوي على "data: "
                if line_str.startswith("data: "):
                    data_str = line_str[6:]  # إزالة "data: "
                    
                    try:
                        data = json.loads(data_str)
                        
                        # استخراج المحتوى من الرسالة
                        if "choices" in data and len(data["choices"]) > 0:
                            if "delta" in data["choices"][0]:
                                delta = data["choices"][0]["delta"]
                                if "content" in delta and delta["content"]:
                                    content = delta["content"]
                                    full_response += content
                                    # طباعة المحتوى مباشرة مع عدم الانتظار
                                    print(content, end="", flush=True)
                                    
                        # عند الانتهاء من الإجابة
                        if "choices" in data and len(data["choices"]) > 0:
                            if "delta" in data["choices"][0]:
                                if "status" in data["choices"][0]["delta"]:
                                    if data["choices"][0]["delta"]["status"] == "finished":
                                        print()  # سطر جديد بعد الانتهاء
                                        break
                                        
                    except json.JSONDecodeError:
                        # تجاهل الأخطاء في تحليل JSON
                        continue
        
        # طباعة الرد الكامل بعد الانتهاء
        print("\n\nالرد الكامل:")
        print(full_response)
        
    else:
        print(f"خطأ في الطلب: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"حدث خطأ: {e}")
