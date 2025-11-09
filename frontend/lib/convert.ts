const handleJsonToCSV = (jsonToCSV, data) => {
    if (data) {
        const results = jsonToCSV(data);
        const rows = results.split("\n");
        const arr: Array<string> = [];
        for (const row of rows) {
            arr.push(row.split(","));
        }
        return arr;
    }
};
export { handleJsonToCSV };
