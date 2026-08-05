import { useEffect, useRef } from "react";
import { Html5QrcodeScanner } from "html5-qrcode";


function BarcodeScanner({ onScan }) {


    const scannerRef = useRef(null);

    const scannedRef = useRef(false);



    useEffect(() => {


        if(scannedRef.current){

            return;

        }



        const scanner = new Html5QrcodeScanner(

            "barcode-reader",

            {

                fps: 10,

                qrbox: {

                    width: 280,

                    height: 160

                },

                aspectRatio: 1.777778,

                rememberLastUsedCamera: true,

                showTorchButtonIfSupported: true

            },

            false

        );



        scannerRef.current = scanner;



        scanner.render(


            async (decodedText) => {


                if(scannedRef.current){

                    return;

                }


                scannedRef.current = true;



                console.log(
                    "Barcode:",
                    decodedText
                );



                // Send barcode back to Scanner.jsx

                onScan(decodedText);



                // Give React time to process

                setTimeout(async ()=>{


                    try {


                        await scanner.clear();


                    } catch(error){


                        console.log(
                            "Scanner cleanup:",
                            error
                        );


                    }


                },500);



            },


            () => {

                // Ignore scan errors

            }


        );





        return () => {


            try {


                if(scannerRef.current){


                    scannerRef.current.clear()

                    .catch(()=>{});


                }


            }

            catch(error){


                console.log(
                    "Scanner destroy:",
                    error
                );


            }



        };


    }, [onScan]);







    return (

        <div className="barcode-camera">


            <div className="camera-header">

                📷 FlipIntel Camera Scanner

            </div>



            <div className="camera-status">

                🔎 Align barcode inside scanner frame

            </div>



            <div

                id="barcode-reader"

            ></div>



        </div>

    );


}


export default BarcodeScanner;