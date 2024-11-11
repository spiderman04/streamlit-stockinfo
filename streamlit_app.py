import streamlit as st
import yfinance as yf

with st.sidebar:
    selected = st.text_input("Enter a stock symbol")
    # start_date = st.date_input("Enter Start Date")
    # start_date = st.date_input("Enter End Date")

    symbol_list = get_symbols_from_file()
    selected = st.selectbox("Pick One*", sorted(symbol_list))
    st.text("*NOTE: Overrides the Symbol field above.")

    # debug st.text("You entered: " + str(selected))
    # st.text("Date entered: " + str(start_date))

st.title("Simple Stock Info Site")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Price Info", "Properties", "Demographics"
                                           , "Avg Pricing","Risk Data", "Graphs"])
tab1.write("Current Price for " + str(selected))
tab1.divider()
if selected is not None:
    result = yfinance.Ticker(selected)
    tab1.write("Previous Close=" + str(result.info.get('previousClose')))
    tab1.write("Open=" + str(result.info.get('open')))
    tab1.write("Volume=" + str(result.info.get('volume')))
    tab1.write("Average Volume=" + str(result.info.get('averageVolume')))
    tab1.divider()

tab2.write("All Properties")
tab2.divider()
for item in result.info.items():
    tab2.write("\t" + item[0] + "=" + str(item[1]))
tab2.divider()
tab2.html("<a target=""_top"">Top WIP</a>")

tab3.write("Basic Demographics")
tab3.divider()
for item in PROPS_DEMOGRAPHICS:
    fetch = result.info.get(item)
    tab3.html("<ul style=""list-style-type:square;"">")
    if item == 'website':
        tab3.html("<li>website=<a href='" + str(fetch) + "'>"+selected+"</a></li")
       #  tab3.link_button(str(result.info.get(item)))
        # tab3.html("<li>" + item + "=<a href="" + str(result.info.get(item)) + "></a></li>")
    else:
        tab3.html("<li>" + item + "=" + str(result.info.get(item)) + "</li>")

tab3.html("</ul>")
tab3.divider()

tab4.write("Average Pricing")
tab4.divider()
for item in PROPS_AVERAGE_PRICING:
    tab4.write("\t" + item +"=" + str(result.info.get(item)))
tab4.divider()
