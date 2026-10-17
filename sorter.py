import time
from typing import Literal

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel,Field

load_dotenv()
client = genai.Client()

class Item(BaseModel):
    text: str = Field(description = "One thing From the dump , as a short Clear line.")
    bucket: Literal["tonight","this_week","later","cant_fix_now"] = Field(
        description = "When this Should be Dealt with."
    )
    why: str = Field(description = "One short reason for this bucket.")

class SortedDump(BaseModel):
    items: list[Item]
    next_step : str = Field(
        description = "The Single Smallest Action to do first .Must take under 15 mins."
    )

RULES = """You help a tired student clear their head.
Split the brain dump below into separate items, one per distinct thing.
Put each item in exactly one bucket:
- tonight: small, or needed to rest tonight
- this_week: has to happen in the next 7 days
- later: goals or plans with no deadline this week
- cant_fix_now: outside their control right now, or a feeling to acknowledge, not a task
Only use things that are in the dump. Never invent new tasks.
Then pick one next_step: the smallest useful action to do first.
Brain dump:
"""

def sort_dump(dump:str)-> SortedDump:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=RULES + dump,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": SortedDump.model_json_schema(),
        },
    )
    return SortedDump.model_validate_json(interaction.output_text)
        
if __name__ == "__main__":
    dump = """infrrd form due soon, fix the numbers on my resume, portfolio timeline,
            dp revision, bda viva prep, plan a trip with my friend, sleep properly,
            the college wifi is down tonight"""

    start = time.perf_counter()
    result = sort_dump(dump)
    seconds = time.perf_counter() - start

    for bucket in ["tonight", "this_week", "later", "cant_fix_now"]:
        print(f"\n== {bucket} ==")
        for item in result.items:
            if item.bucket == bucket:
                print(f"- {item.text}  ({item.why})")

    print(f"\nNext step: {result.next_step}")
    print(f"Took {seconds:.1f} s")
