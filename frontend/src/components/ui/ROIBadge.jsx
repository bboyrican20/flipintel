function ROIBadge({ roi }) {

    const formattedROI =
        Number(roi ?? 0).toFixed(2);


    return (

        <span className="roi-badge">

            🚀 {formattedROI}% ROI

        </span>

    );

}


export default ROIBadge;