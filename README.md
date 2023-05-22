# Steps for QA with Hugging Face

Used model - https://huggingface.co/distilbert-base-cased-distilled-squad

Deployed using Streamlit

To run it as a API service:
python.exe ./src/api.py

To run it as a streamlit webapp:
python.exe -m streamlit run ./src/webapp.py

URL : https://mallapraveen-atomstate-interview--srcwebapp-mx26ad.streamlit.app/
Github Repo : https://github.com/mallapraveen/atomstate-interview

Or If you want as API service, I have written fastapi code as well which can be run by the below command.
python.exe ./src/api.py

Swagger implementation can found at : http://localhost:8000/docs

Below is a sample for Json object sent as POST request.

curl -X 'POST' \
 'http://localhost:8000/qa' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
"question": "What city is Spiderman located in?",
"context": "In a stunning crossover event, Spider-Man swung through the bustling streets of New York City, only to find himself facing a formidable foe. Just as he was about to be overwhelmed, a streak of blue and red blurred past him, and there stood the legendary Superman. The two heroes joined forces, their powers complementing each other perfectly. Together, they fought side by side, vanquishing the villain with unwavering determination. As the battle concluded, Spider-Man extended his hand to Superman, a newfound respect between Marvel and DC forming. Their encounter served as a testament to the unbreakable bond heroes share, transcending universes and inspiring hope for all."
}'
