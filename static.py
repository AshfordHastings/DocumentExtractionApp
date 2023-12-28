

SIMPLE_EXTRACTION_TEMPLATE = """
{format_instructions}
Extract and identify the relevant entities and their properties from the passage below. Remember, only include properties mentioned in the schema and format your response as a simple JSON object.

Passage:
{context}
"""

SIMPLE_FORMAT_INSTRUCTIONS = """

"Based on the following information, please provide a response strictly in JSON format according to the given schema. Do not include any additional text or explanations, just the JSON object.

```
{schema}
```"""

# SIMPLE_EXTRACTION_TEMPLATE = """
# {format_instructions}
# Extract and save the relevant entities mentioned \
# in the following passage together with their properties.

# Only extract the relevent properties. Only return the specified extraction according to the schema.

# If a property is not present and is not required in the function parameters, do not include it in the output.

# Passage:
# {context}
# """

# SIMPLE_FORMAT_INSTRUCTIONS = """The output should be formatted as a JSON instance that conforms to the JSON schema below.

# As an example, for the schema {{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}
# the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of the schema. The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.

# Please provide the information in a JSON format.

# Here is the output schema:
# ```
# {schema}
# ```"""