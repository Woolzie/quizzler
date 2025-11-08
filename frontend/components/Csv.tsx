import React, { CSSProperties } from "react";
import { useCSVReader } from "react-papaparse";

const styles = {
    csvReader: {
        display: "flex",
        flexDirection: "row",
        marginBottom: 10,
    } as CSSProperties,
    browseFile: {
        width: "20%",
    } as CSSProperties,
    acceptedFile: {
        border: "1px solid #ccc",
        height: 45,
        lineHeight: 2.5,
        paddingLeft: 10,
        width: "80%",
    } as CSSProperties,
    remove: {
        borderRadius: 0,
        padding: "0 20px",
    } as CSSProperties,
    //     progressBarBackgroundColor: {
    //         backgroundColor: "red",
    //     } as CSSProperties,
};

type ICSVReader = {
    setInputCsv: React.Dispatch<React.SetStateAction<object>>;
};
export default function CSVReader({ setInputCsv }) {
    const { CSVReader } = useCSVReader();

    return (
        <CSVReader
            onUploadAccepted={(results: any) => {
                setInputCsv(results);
            }}
        >
            {({
                getRootProps,
                acceptedFile,
                ProgressBar,
                getRemoveFileProps,
            }: any) => (
                <>
                    <div style={styles.csvReader}>
                        <button
                            {...getRootProps()}
                            className="border p-3 rounded-xl"
                        >
                            Upload csv
                        </button>
                    </div>
                </>
            )}
        </CSVReader>
    );
}
