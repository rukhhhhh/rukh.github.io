# iOS Financial Tracker

I came up with this Financial Tracker as I got tired of manually logging my daily expenses into a sheet. I thought that the best quality of life improvement would be to be able to run a logging script using the iPhone Shortcuts app. The input will be the Action button in iPhone 15 & above. This project is not documented in full; the full capability consists of it exporting each sheet at the end of each month to an annual expense tracker.


## Table of Contents

* [iOS Shorcuts](#ios-shortcuts)

### iOS Shortcuts

Using the shortcuts app and a little bit of research, I came up with a script that runs when activated with the action button. 

```html
<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<meta name="format-detection" content="telephone=no,date=no">
<title>Finance Tracker</title>
<style>
body {
	font-family: system-ui;
	font-size: 0.95em;
	margin-top: 1rem;
	margin-bottom: calc(1rem + env(safe-area-inset-bottom));
	word-break: break-word;
}

button {
	color: #000;
	background-color: #e4e4ff;
	width: 100%;
	font-size: 1em;
	font-weight: normal;
	line-height: 1.8;
	text-align: left;
	margin: 4px 0;
	padding: 1px 8px;
	border: 1px #aaa;
	border-style: solid;
	border-radius: 8px;
	cursor: initial;
	touch-action: manipulation;
}

.button {
	margin-bottom: 0;
	border-bottom-style: none;
	border-bottom-left-radius: 0;
	border-bottom-right-radius: 0;
	cursor: auto;
}
.button::after {
	content: '\25A1';
	float: right;
	font-weight: bold;
	margin-left: 10px;
}

.closed {
	margin-bottom: 4px;
	border-bottom-style: solid;
	border-bottom-left-radius: 8px;
	border-bottom-right-radius: 8px;
}
.closed::after { content: '\2212'; }

.nonbottom {
	margin-bottom: 0;
	border-bottom-left-radius: 0;
	border-bottom-right-radius: 0;
	border-bottom-style: none;
}
.nontop {
	margin-top: 0;
	border-top-left-radius: 0;
	border-top-right-radius: 0;
}

.gGray { background-color: #e0e0e0; }
.gGreen { background-color: #ddffdd; }
.gYellow { background-color: #ffeebb; }
.gOrange { background-color: #ffddcc; }
.gRed { background-color: #ffccdd; }
.gBlue { background-color: #aaccff; }
.gUnknown { background-color: #bbffff; }
.gApple { background-color: #f6f6ff; }
.gParams {
	text-align: center;
	background-color: #f8f8f8;
}

.content {
	overflow: hidden;
	margin-bottom: 4px;
	padding: 3px 0 3px 8px;
	border: 1px #aaa;
	border-style: none solid solid solid;
	border-bottom-left-radius: 8px;
	border-bottom-right-radius: 8px;
}

.contentloop {
	margin-bottom: 0;
	padding-top: 4px;
	padding-bottom: 4px;
	border-bottom-style: none;
	border-bottom-left-radius: 0;
	border-bottom-right-radius: 0;
}

.dotted { border-left-style: dotted; }
.dashed { border-left-style: dashed; }

.inside {
	border-right-style: none;
	border-top-right-radius: 0;
	border-bottom-right-radius: 0;
}

.commentcontent { background-color: #ffeebb; }

.row {
	display: flex;
	padding-right: 2px;
}

.col1 {
	margin-right: 3px;
	padding-right: 3px;
	border-right-style: double;
}
.col2 { white-space: pre-wrap; }

span.box {
	display: inline;
	white-space: pre-wrap;
	margin: 2px;
	padding: 2px 4px;
	border-radius: 6px;
	background-color: #fff;
}
span.var { font-style: italic; }
span.magic {
	cursor: pointer;
	font-style: italic;
	text-decoration: underline;
}

hr {
	width: 0px;
	height: 2px;
	border: 1px solid #aaa;
	margin: -4px auto;
}

@media (prefers-color-scheme: dark) {
	body { background: #000; color: #eee; }
	button { background: #514c72; color: #eee; }
	.gGray { background-color: #555555; }
	.gGreen { background-color: #3a6441; }
	.gYellow { background-color: #716d33; }
	.gOrange { background-color: #76523f; }
	.gRed { background-color: #674044; }
	.gBlue { background-color: #384c67; }
	.gUnknown { background-color: #377172; }
	.gApple { background-color: #2c2842; }
	.gParams { background-color: #181818; }
	.commentcontent { background-color: #716d33; }
	span.box { background-color: #000; }
}
</style></head><body>
<button class="button gParams"><b>Finance Tracker</b> (<span class="magic" onclick="magictap(112)">113</span> actions, 13 KB)</button><div class="content">
<div class="col2">"WFQuickActionSurfaces": [],
"WFWorkflowClientVersion": "3607.0.2",
"WFWorkflowHasOutputFallback": false,
"WFWorkflowHasShortcutInputVariables": false,
"WFWorkflowIcon": {
   "WFWorkflowIconStartColor": 2846468607,
   "WFWorkflowIconGlyphNumber": 59395
},
"WFWorkflowImportQuestions": [
   {
      "ParameterKey": "WFTextActionText",
      "Category": "Parameter",
      "ActionIndex": <span class="magic" onclick="magictap(48)"><b>48</b></span>,
      "Text": "Webappid?"
   }
],
"WFWorkflowInputContentItemClasses": [
   "WFAppStoreAppContentItem",
   "WFArticleContentItem",
   "WFContactContentItem",
   "WFDateContentItem",
   "WFEmailAddressContentItem",
   "WFGenericFileContentItem",
   "WFImageContentItem",
   "WFiTunesProductContentItem",
   "WFLocationContentItem",
   "WFDCMapsLinkContentItem",
   "WFAVAssetContentItem",
   "WFPDFContentItem",
   "WFPhoneNumberContentItem",
   "WFRichTextContentItem",
   "WFSafariWebPageContentItem",
   "WFStringContentItem",
   "WFURLContentItem"
],
"WFWorkflowMinimumClientVersion": <span style="color:red">3010</span>,
"WFWorkflowMinimumClientVersionString": "<span style="color:red">3010</span>",
"WFWorkflowOutputContentItemClasses": [],
"WFWorkflowTypes": [
   "Watch",
   "NCWidget"
]
</div></div>
<button class="button gYellow" id="m0">
0 Text</button><div class="content">
<div class="col2">Sharukh Khan</div></div>
<button class="button gGray nonbottom" id="m1">
1 Choose from Menu</button><div class="content contentloop">
<div class="row"><div class="col1">MenuPrompt</div><span style="display:none">: </span><div class="col2">Expense or Income:<b>\u{space}</b></div></div>
<div class="row"><div class="col1">MenuItems</div><span style="display:none">: </span><div class="col2">[Expense,
Income]</div></div></div>
<button class="button gGray nonbottom nontop" id="m2">
2 Menu Item <span class="box">Expense</span></button><div class="content contentloop">
<button class="button gYellow inside" id="m3">
3 Text　»</button><div class="content inside">
<div class="col2">expense</div></div>
<hr><button class="gOrange inside" id="m4">
4 Set Variable <span class="box">expenditure</span> to <span class="box"><span class="var"><b>[3 Text]</b></span></span></button><div></div>
<button class="button gGray nonbottom inside" id="m5">
5 Choose from Menu</button><div class="content contentloop dotted inside">
<div class="row"><div class="col1">MenuPrompt</div><span style="display:none">: </span><div class="col2">Category:<b>\u{space}</b></div></div>
<div class="row"><div class="col1">MenuItems</div><span style="display:none">: </span><div class="col2">[Transportation,
Food,
Entertainment,
Bills,
Gifts,
Personal,
Health,
Travel,
Miscellaneous<b>\u{space}</b>]</div></div></div>
<button class="button gGray nonbottom nontop inside" id="m6">
6 Menu Item <span class="box">Transportation</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m7">
7 Text　»</button><div class="content inside">
<div class="col2">Transportation</div></div>
<hr><button class="gOrange inside" id="m8">
8 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[7 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m9">
9 Menu Item <span class="box">Food</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m10">
10 Text　»</button><div class="content inside">
<div class="col2">Food</div></div>
<hr><button class="gOrange inside" id="m11">
11 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[10 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m12">
12 Menu Item <span class="box">Entertainment</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m13">
13 Text　»</button><div class="content inside">
<div class="col2">Entertainment</div></div>
<hr><button class="gOrange inside" id="m14">
14 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[13 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m15">
15 Menu Item <span class="box">Bills</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m16">
16 Text　»</button><div class="content inside">
<div class="col2">Bills</div></div>
<hr><button class="gOrange inside" id="m17">
17 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[16 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m18">
18 Menu Item <span class="box">Gifts</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m19">
19 Text　»</button><div class="content inside">
<div class="col2">Gifts</div></div>
<hr><button class="gOrange inside" id="m20">
20 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[19 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m21">
21 Menu Item <span class="box">Personal</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m22">
22 Text　»</button><div class="content inside">
<div class="col2">Personal</div></div>
<hr><button class="gOrange inside" id="m23">
23 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[22 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m24">
24 Menu Item <span class="box">Health</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m25">
25 Text　»</button><div class="content inside">
<div class="col2">Health</div></div>
<hr><button class="gOrange inside" id="m26">
26 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[25 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m27">
27 Menu Item <span class="box">Travel</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m28">
28 Text　»</button><div class="content inside">
<div class="col2">Travel</div></div>
<hr><button class="gOrange inside" id="m29">
29 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[28 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m30">
30 Menu Item <span class="box">Miscellaneous<b>\u{space}</b></span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m31">
31 Text　»</button><div class="content inside">
<div class="col2">Other</div></div>
<hr><button class="gOrange inside" id="m32">
32 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[31 Text]</b></span></span></button></div>
<button class="gGray nontop inside" id="m33">
33 End Menu</button></div>
<button class="button gGray nonbottom nontop" id="m34">
34 Menu Item <span class="box">Income</span>　▵<span class="magic" onclick="magictap(2)">2</span></button><div class="content contentloop">
<button class="button gYellow inside" id="m35">
35 Text　»</button><div class="content inside">
<div class="col2">income</div></div>
<hr><button class="gOrange inside" id="m36">
36 Set Variable <span class="box">expenditure</span> to <span class="box"><span class="var"><b>[35 Text]</b></span></span></button><div></div>
<button class="button gGray nonbottom inside" id="m37">
37 Choose from Menu</button><div class="content contentloop dotted inside">
<div class="row"><div class="col1">MenuPrompt</div><span style="display:none">: </span><div class="col2">Select:<b>\u{space}</b></div></div>
<div class="row"><div class="col1">MenuItems</div><span style="display:none">: </span><div class="col2">[Savings,
Salary,
PayNow / Bank Transfer,
Deposit,
Bonus,
Other]</div></div></div>
<button class="button gGray nonbottom nontop inside" id="m38">
38 Menu Item <span class="box">Savings</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m39">
39 Text　»</button><div class="content inside">
<div class="col2">Savings</div></div>
<hr><button class="gOrange inside" id="m40">
40 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[39 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m41">
41 Menu Item <span class="box">Salary</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m42">
42 Text　»</button><div class="content inside">
<div class="col2">Salary</div></div>
<hr><button class="gOrange inside" id="m43">
43 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[42 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m44">
44 Menu Item <span class="box">PayNow / Bank Transfer</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m45">
45 Text　»</button><div class="content inside">
<div class="col2">PayNow</div></div>
<hr><button class="gOrange inside" id="m46">
46 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[45 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m47">
47 Menu Item <span class="box">Deposit</span></button><div class="content contentloop dotted inside">
<button class="gYellow inside" id="m48">
48 Text　»</button>
<hr><button class="gOrange inside" id="m49">
49 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[48 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m50">
50 Menu Item <span class="box">Bonus</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m51">
51 Text　»</button><div class="content inside">
<div class="col2">Bonus</div></div>
<hr><button class="gOrange inside" id="m52">
52 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[51 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m53">
53 Menu Item <span class="box">Other</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m54">
54 Text　»</button><div class="content inside">
<div class="col2">Other</div></div>
<hr><button class="gOrange inside" id="m55">
55 Set Variable <span class="box">category</span> to <span class="box"><span class="var"><b>[54 Text]</b></span></span></button></div>
<button class="gGray nontop inside" id="m56">
56 End Menu</button></div>
<button class="gGray nontop" id="m57">
57 End Menu　▵<span class="magic" onclick="magictap(34)">34</span></button><div></div>
<button class="button " id="m58">
58 Ask for <span class="box">Number</span> Input　»</button><div class="content">
<div class="row"><div class="col1">AskActionAllowsNegativeNumbers</div><span style="display:none">: </span><div class="col2">false</div></div>
<div class="row"><div class="col1">AskActionPrompt</div><span style="display:none">: </span><div class="col2">Amount?</div></div></div>
<hr><button class="gOrange" id="m59">
59 Set Variable <span class="box">amount</span> to <span class="box"><span class="var"><b>[58 Ask for Input]</b></span></span></button><div></div>
<button class="button gGray nonbottom" id="m60">
60 If <span class="box"><span class="var"><b>[expenditure]</b></span></span> <span class="box">is</span> <span class="box">income</span></button><div class="content contentloop">
<button class="button gGray nonbottom inside" id="m61">
61 If <span class="box">Any</span> are true<br/>　<span class="box"><span class="var"><b>[category]</b></span></span> <span class="box">is</span> <span class="box">Savings</span><br/>　<span class="box"><span class="var"><b>[category]</b></span></span> <span class="box">is</span> <span class="box">Salary</span><br/>　<span class="box"><span class="var"><b>[category]</b></span></span> <span class="box">is</span> <span class="box">Bonus</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m62">
62 Text　»</button><div class="content inside">
<div class="col2">Bank%20Transfer</div></div>
<hr><button class="gOrange inside" id="m63">
63 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[62 Text]</b></span></span></button></div>
<button class="gGray nontop inside" id="m64">
64 End If</button><div></div>
<button class="button gGray nonbottom inside" id="m65">
65 If <span class="box"><span class="var"><b>[category]</b></span></span> <span class="box">is</span> <span class="box">PayNow</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m66">
66 Text　»</button><div class="content inside">
<div class="col2">PayNow</div></div>
<hr><button class="gOrange inside" id="m67">
67 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[66 Text]</b></span></span></button></div>
<button class="gGray nontop inside" id="m68">
68 End If</button><div></div>
<button class="button gGray nonbottom inside" id="m69">
69 If <span class="box"><span class="var"><b>[category]</b></span></span> <span class="box">is</span> <span class="box">Deposit</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m70">
70 Text　»</button><div class="content inside">
<div class="col2">Cash</div></div>
<hr><button class="gOrange inside" id="m71">
71 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[70 Text]</b></span></span></button></div>
<button class="gGray nontop inside" id="m72">
72 End If</button><div></div>
<button class="button gGray nonbottom inside" id="m73">
73 If <span class="box"><span class="var"><b>[category]</b></span></span> <span class="box">is</span> <span class="box">Other</span></button><div class="content contentloop dotted inside">
<button class="button gGray nonbottom inside" id="m74">
74 Choose from Menu</button><div class="content contentloop dashed inside">
<div class="row"><div class="col1">MenuPrompt</div><span style="display:none">: </span><div class="col2">Mode:<b>\u{space}</b></div></div>
<div class="row"><div class="col1">MenuItems</div><span style="display:none">: </span><div class="col2">[PayNow,
Bank Transfer,
Cash]</div></div></div>
<button class="button gGray nonbottom nontop inside" id="m75">
75 Menu Item <span class="box">PayNow</span></button><div class="content contentloop dashed inside">
<button class="button gYellow inside" id="m76">
76 Text　»</button><div class="content inside">
<div class="col2">PayNow</div></div>
<hr><button class="gOrange inside" id="m77">
77 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[76 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m78">
78 Menu Item <span class="box">Bank Transfer</span></button><div class="content contentloop dashed inside">
<button class="button gYellow inside" id="m79">
79 Text　»</button><div class="content inside">
<div class="col2">Bank Transfer</div></div>
<hr><button class="gOrange inside" id="m80">
80 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[79 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m81">
81 Menu Item <span class="box">Cash</span></button><div class="content contentloop dashed inside">
<button class="button gYellow inside" id="m82">
82 Text　»</button><div class="content inside">
<div class="col2">Cash</div></div>
<hr><button class="gOrange inside" id="m83">
83 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[82 Text]</b></span></span></button></div>
<button class="gGray nontop inside" id="m84">
84 End Menu</button></div>
<button class="gGray nontop inside" id="m85">
85 End If　▵<span class="magic" onclick="magictap(73)">73</span></button></div>
<button class="button gGray nonbottom nontop" id="m86">
86 Otherwise　▵<span class="magic" onclick="magictap(60)">60</span></button><div class="content contentloop">
<button class="button gGray nonbottom inside" id="m87">
87 Choose from Menu</button><div class="content contentloop dotted inside">
<div class="row"><div class="col1">MenuPrompt</div><span style="display:none">: </span><div class="col2">Payment Mode:<b>\u{space}</b></div></div>
<div class="row"><div class="col1">MenuItems</div><span style="display:none">: </span><div class="col2">[NetsQR,
PayNow,
Visa,
Cash]</div></div></div>
<button class="button gGray nonbottom nontop inside" id="m88">
88 Menu Item <span class="box">NetsQR</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m89">
89 Text　»</button><div class="content inside">
<div class="col2">NetsQR</div></div>
<hr><button class="gOrange inside" id="m90">
90 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[89 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m91">
91 Menu Item <span class="box">PayNow</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m92">
92 Text　»</button><div class="content inside">
<div class="col2">PayNow</div></div>
<hr><button class="gOrange inside" id="m93">
93 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[92 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m94">
94 Menu Item <span class="box">Visa</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m95">
95 Text　»</button><div class="content inside">
<div class="col2">Visa</div></div>
<hr><button class="gOrange inside" id="m96">
96 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[95 Text]</b></span></span></button></div>
<button class="button gGray nonbottom nontop inside" id="m97">
97 Menu Item <span class="box">Cash</span></button><div class="content contentloop dotted inside">
<button class="button gYellow inside" id="m98">
98 Text　»</button><div class="content inside">
<div class="col2">Cash</div></div>
<hr><button class="gOrange inside" id="m99">
99 Set Variable <span class="box">account</span> to <span class="box"><span class="var"><b>[98 Text]</b></span></span></button></div>
<button class="gGray nontop inside" id="m100">
100 End Menu</button></div>
<button class="gGray nontop" id="m101">
101 End If　▵<span class="magic" onclick="magictap(86)">86</span></button><div></div>
<button class="button " id="m102">
102 Ask for Text Input　»</button><div class="content">
<div class="row"><div class="col1">AskActionPrompt</div><span style="display:none">: </span><div class="col2">Description:<b>\u{space}</b></div></div>
<div class="row"><div class="col1">AskActionDefaultAnswer</div><span style="display:none">: </span><div class="col2"></div></div></div>
<hr><button class="gYellow" id="m103">
103 Get Text from <span class="box"><span class="var"><b>[102 Ask for Input]</b></span></span>　»</button>
<hr><button class="gBlue" id="m104">
104 URL Encode <span class="box"><span class="var"><b>[103 Text]</b></span></span>　»</button>
<hr><button class="gOrange" id="m105">
105 Set Variable <span class="box">detail</span> to <span class="box"><span class="var"><b>[104 URL Encoded Text]</b></span></span></button><div></div>
<button class="button gYellow" id="m106">
106 Text　»</button><div class="content">
<div class="col2"></div></div>
<hr><button class="gOrange" id="m107">
107 Set Variable <span class="box">webappid</span> to <span class="box"><span class="var"><b>[106 Text]</b></span></span></button><div></div>
<button class="button gYellow" id="m108">
108 Text　»</button><div class="content">
<div class="col2">https://script.google.com/macros/s/<span class="var"><b>[webappid]</b></span>/exec?amount=<span class="var"><b>[amount</b> as Text<b>]</b></span>&amp;expenditure=<span class="var"><b>[expenditure]</b></span>&amp;account=<span class="var"><b>[account</b> as Text<b>]</b></span>&amp;category=<span class="var"><b>[category</b> as Text<b>]</b></span>&amp;detail=<span class="var"><b>[detail]</b></span></div></div>
<hr><button class="gBlue" id="m109">
109 Get URLs from <span class="box"><span class="var"><b>[108 Text]</b></span></span>　»</button>
<hr><button class="button gGreen" id="m110">
110 Get Contents of URL <span class="box"><span class="var"><b>[109 URLs]</b></span></span>　»</button><div class="content">
<div class="row"><div class="col1">Advanced</div><span style="display:none">: </span><div class="col2">true</div></div>
<div class="row"><div class="col1">HTTPHeaders</div><span style="display:none">: </span><div class="col2">{}</div></div>
<div class="row"><div class="col1">ShowHeaders</div><span style="display:none">: </span><div class="col2">true</div></div>
<div class="row"><div class="col1">HTTPMethod</div><span style="display:none">: </span><div class="col2">GET</div></div></div>
<hr><button class="button gYellow" id="m111">
111 Show Result</button><div class="content">
<div class="col2"><span class="var"><b>[110 Contents of URL]</b></span></div></div>
<button class="button gRed" id="m112">
112 Vibrate Device</button><div class="content">
<div class="row"><div class="col1">VibrateHapticType</div><span style="display:none">: </span><div class="col2">Up Direction</div></div></div>
<script>
for (b of document.getElementsByClassName('button')) {
	b.addEventListener('click', function() {
		this.classList.toggle('closed');
		let s = this.nextElementSibling;
		s.style.display = getComputedStyle(s).display==='none' ? 'block' : 'none';
})}

function magictap(id) {
	event.stopPropagation();
	let e = document.getElementById('m'+id);
	let p = e;
	while ((p = p.parentNode).tagName.toLowerCase() === 'div') {
		p.style.display = 'block';
		p.previousElementSibling.classList.remove('closed');
	}
	setTimeout(function(){ e.scrollIntoView({block:'nearest',behavior:'smooth'}); }, 10);
}
</script></body></html>
```
