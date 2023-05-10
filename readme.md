<h1>Database Querying with Flask</h1>
<h3>Zayn Severance, 05/10/2023</h3>
<hr>
<h3>Overview</h3>
<p>I'll admit, I had some experience with Flask but almost none with json.
I spent maybe an hour on the flask part, and then a good three or four on the json stuff.<br>
Regardless, this program is designed to return data from the csv given when queried properly.
</p>
<h3>Install and Run instructions</h3>
<ul>
<li>`git clone https://github.com/The-Mad-Duck/support-software-interview-exercise-01`</li>
<li>run setup.py</li>
<li>run main.py</li>
<li>query website using proper localhost port</li>
</ul>

<h3>Filter Keywords</h3>
<li>`[submitted_after]=` (ISO 8601 datetime) - return only records submitted on or after the given date</li>
<li>`[submitted_before]=` (ISO 8601 datetime) - return only records submitted on or before the given date</li>
<li>`[min_nodes]=` (integer) - return only records that used at least the given number of nodes</li>
<li>`[max_nodes]=` (integer) - return only records that used at most the given number of nodes</li>

<h3>What can be improved</h3>
<ul>
<li>Trying to use `+` in the URL doesn't work, 
the only thing found on this is a Stack Overflow post blaming the URL itself 
because `+` is normally reserved for spaces. Instead, use `%2B` which is the encoding for `+`.</li>
<li>Querying can't just use `localhost`, a port has to be set.</li>
<li>Formatting the json file feels slow and unoptimized.</li>
</ul>