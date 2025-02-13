from langchain_core.prompts import PromptTemplate

class Prompts:
    VALIDATE_RETRIEVAL = PromptTemplate(
        input_variables=["retrieved_context", "question", "curr_round", "max_rounds"],
        template="""
        You are a retrieval validator.
        You will be provided with a question and chunks of text that may or may not contain the answer to the question.
        Your role is to carefullylook through the chunks of text provide a JSON response with three fields:
        1. status: whether the retrieved chunks contain the answer to the question.
        - 'COMPLETE' if the retrieved chunks contain the answer to the question, 'INCOMPLETE' otherwise. Nothing else.
        
        2. useful_information: the useful information from the retrieved chunks. Be concise and direct.
        - if there is no useful information, set this to an empty string.
        
        3. missing_information: the missing information that is needed to answer the question in full. Be concise and direct.
        - if there is no missing information, set this to an empty string.
        
        Please provide your response as dictionary in the followingformat.

        {{"status": "<status>",
        "useful_information": "<useful_information>",
        "missing_information": "<missing_information>"}}
        
        Here is an example of the response format:
        
        {{"status": "COMPLETE",
        "useful_information": "The capital city of Canada is Ottawa.",
        "missing_information": "The capital city of Mexico"}}
    
        Do not include any other text.
        
        Context: {retrieved_context}
        
        The Question: {question}

        IMPORTANT: you are on round {curr_round} of {max_rounds} we must not go the {max_rounds} rounds. So if you are on round {max_rounds} you MUST return "COMPLETE"
    
        
        Response:
        """
    )
    ANSWER_QUESTION = PromptTemplate(
        input_variables=["retrieved_context", "question"],
        template="""
        You are a question answering agent.
        You will be provided with a question and chunks of text that contain the answer to the question.
        Your role is to carefully look through the chunks of text and answer the question.
        Provide a direct and concise answer based on the information provided.
        Do not include any additional information or commentary.
        
        The Question: {question}
        Context: {retrieved_context}
        Answer:
        """
    )
