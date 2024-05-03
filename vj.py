# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Viju",
        page_icon=":flag-no:",
    )

st.image('Viju.png')
st.write("# Viju Vinod Kanna R!")


col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/vijuvinodkanna/",use_container_width=True )
    st.link_button("Ivanna Shalom", "https://www.ivannashalom.com/",use_container_width=True )

    
with col2:
    st.link_button("Instagram", "https://www.instagram.com/viju0077/?hl=en",use_container_width=True)
    st.link_button("Raj Kumar", "https://www.ivannashalom.com/rajkumar",use_container_width=True )

    

with col3:
    st.link_button("Facebook", "https://www.facebook.com/viju0077",use_container_width=True)
    st.link_button("King Of Kings", "https://www.ivannashalom.com/kingofkings",use_container_width=True )    




#if __name__ == "__main__":
 #   run():