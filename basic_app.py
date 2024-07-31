"""
Basic Streamlit Demonstration

"""
import streamlit as st

st.title("Hello World")

st.write("""

# My first app. Hello world!

""")

st.write(':smiley:')


st.write("""

## markdown header h2

- unordered list item 1
- unordered list item 2

1. ordered list
2. ordered list

```python
print('hey!')
```

```sql
SELECT *
FROM my_table
LIMIT 10;
```

""")
