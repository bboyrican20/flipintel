function AIScore({
    score = 95,
    reasons = [],
    recommendation = "BUY NOW"
}){


return (

<div className="ai-score-card">


<div className="ai-score-header">


<h2>
🤖 AI Confidence
</h2>


<div className="confidence-number">

{score}/100

</div>


</div>





<div className="confidence-bar">


<div

className="confidence-fill"

style={{
width:`${score}%`
}}

>


</div>


</div>







<h3>

Why FlipIntel Likes This

</h3>





<ul>


{

reasons.length > 0

?

reasons.map((reason,index)=>(


<li key={index}>

✅ {reason}

</li>


))


:

<>


<li>
✅ Strong profit margin
</li>


<li>
✅ Market demand detected
</li>


<li>
✅ Low risk category
</li>


</>


}


</ul>








<div className="ai-recommendation">


🔥 {recommendation}


</div>





</div>


);


}


export default AIScore;