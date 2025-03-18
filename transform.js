function parseCSVLine(line) {
    const regex = /"([^"]*)"|([^,]+)/g;
    let values = [];
    let match;
    
    while ((match = regex.exec(line)) !== null) {
        values.push(match[1] || match[2]); // Extract quoted or unquoted values
    }

    return values;
}

function transform(line) {
    var values = parseCSVLine(line);

    if (!values || values[0].toLowerCase() === 'statename') {
        return null;
    }

    var obj = {
        StateName: values[0],
        DistrictName: values[1],
        Commodity: values[2],
        MarketName: values[3],
        Variety: values[4],
        Group: values[5],
        ArrivalsTonnes: parseFloat(values[6]),
        MinPriceRsPerQuintal: parseFloat(values[7]),
        MaxPriceRsPerQuintal: parseFloat(values[8]),
        ModalPriceRsPerQuintal: parseFloat(values[9]),
        ReportedDate: values[10]
    };

    return JSON.stringify(obj);
}
