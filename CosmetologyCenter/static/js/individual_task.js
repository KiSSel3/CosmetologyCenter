function findOwners() {
    const data = document.getElementById('data').value.trim();
    const owners = {};

    // Разделение введенных данных на строки и обработка каждой строки
    const lines = data.split('\n');
    lines.forEach(line => {
        const [lastName, plotNumber, area] = line.split(' ');
        if (!owners[lastName]) {
            owners[lastName] = {
                plots: [],
                totalArea: 0
            };
        }
        owners[lastName].plots.push(plotNumber);
        owners[lastName].totalArea += parseFloat(area);
    });

    let resultHTML = '<h3>Владельцы с несколькими участками:</h3>';

    for (const owner in owners) {
        if (owners[owner].plots.length > 1) {
            resultHTML += `<p><strong>${owner}</strong>: Участки ${owners[owner].plots.join(', ')}, Общая площадь: ${owners[owner].totalArea} кв.м.</p>`;
        }
    }

    document.getElementById('result').innerHTML = resultHTML;
}