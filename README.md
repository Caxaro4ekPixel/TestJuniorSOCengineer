<b>env parameters:</b> 
(<a href="https://core.telegram.org/api/obtaining_api_id">create application</a>)
<ul>
    <li>api_id - id of your application;</li>
    <li>api_hash - hash of your application;</li>
    <li>username - username of your application;</li>
    <li>chats - urls of your channels and chats (delimiter - ",")</li>
</ul>
<br><br>
<b>What is contained in each in each folder:</b>
<ul>
    <li>logs_tg - contains logs from channels</li>
    <li>screenshots - contains screenshots from Splunk</li>
    <li>splunk_app - contains app Splunk</li>
    <li>temp_date_files - contains channel files (with the last logs date) P.S. the solution is not the most optimal, but it works</li>
</ul>
<br><br>
<b>Description of the principle of operation:</b><br>
The script is fixated on collecting logs every hour (from the list of channels \ chats), and writing to a file (I couldn't find how to machine write to slump after rereading the documentation). That is, it is enough to run it and the logs will be updated (and appended)
<br><br>
Answers to questions:
<br><br>
- <b>How collected data can help the Security team in case of Security Incidents?</b><br>
- According to this data, it is possible to determine who, when and under what circumstances could have committed a violation of the company's rules or privacy policy.<br><br>
- <b>Can we collect any additional data to enrich collected events?</b><br>
- It is possible to collect information not only on the administration and their actions, but also participation in the "discussion" with users (which, when analyzed, may help to identify any additional facts)<br><br>
- <b>What use cases / correlations / alerts the Security team can make using the collected data?</b><br>
- Determine the unfair use of the administrator's rights, the exercise of their powers or the use of the channel for their own purposes (example: placement of uncoordinated advertising)<br><br>
- <b>Any additional thoughts you consider relevant</b><br>
- Data analysis and collection is limited by the Telegram API, but the possibilities of data analysis and processing for security purposes are almost unlimited. (I had experience in such a situation, collecting information about users in the telegram channel to analyze the user's goals and prevent unfair actions, I used the Elasticsearch system for collecting and analyzing)