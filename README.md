# DF-Query-Assistant
Using pandas and OpenAI's API, we can query data in a similar way to SQL - extracting insights and information.

---------------------------------------------------------------------------------------------------------------------------------------

Goals for this project:

I want QBot to essentially be a easy to use, reliable helper for querying a dataset. It should be able to take in files that SQL
or Pandas can read, decide on if SQL or Pandas would be a more reliable querying tool, then use that tool to query the data.

As of right now, it can query a loan_application dataset and return back reasonable responses depending on the phrasing. It
relies on Pandas to do all the computations, which is fine, but if there were to be more complex relational databases I think it
would struggle. This is why I want to incorporate SQL.

By the end of this project, I want it to be wrapped in a simple, sleek user interface where you can:
1. Easily upload a dataset.
2. Type in your query. (Ex. Tell me the average loan amount across rows 1-50.)
3. Get a fast, reasonably accurate response.


How to get there:
I think in order to get SQL into the mix, I might need to wrap both my pandas function and my SQL function into a if statement.
This would mean something like:
If:
    dataset = .csv, .xlsx, etc, use def pdbot()
elif:
    dataset = .SQL, .db, etc, use def sqlbot()

However it's done, I think it'd be pretty cool. It would be even cooler if it could do some basic visualizations too.
Something like "Whats the average loan amount? Create a line chart showing loan amount on the Y axis and year on the x axis.
    Make sure each point is related to its counterpart." 
Or something like that.
Definitely would be rad but focus on getting SQL into the mix first.
