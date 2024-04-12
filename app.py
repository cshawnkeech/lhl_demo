"""
demo page
"""

import streamlit as st

st.title('Hello World')

st.write('This is a simple Streamlit app.')
st.write(':smiley:')

st.markdown("""
## markdown header h2

- unordered list 1
- unordered list 2

```python
print('Hey!')
```

```sql
SELECT *
FROM table_name
LIMIT 10;

```


""")
