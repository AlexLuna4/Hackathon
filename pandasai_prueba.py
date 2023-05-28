import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

df = pd.     ({
   
})

OPENAI_API_KEY = "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"
llm = OpenAI(api_token=OPENAI_API_KEY)

pandas_ai = PandasAI(llm)
print(pandas_ai.run(df, prompt='Which are the 5 happiest countries?'))

pandas_ai.run(df, "Plot the histogram of countries showing for each the gpd, using different colors for each bar")