function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function createTable(size) {
    const table = document.getElementById('myTable');
    table.innerHTML = ''; // Clear the table

    for (let i = 0; i < size; i++) {
        const row = table.insertRow();
        for (let j = 0; j < size; j++) {
            const cell = row.insertCell();
            cell.textContent = getRandomInt(1, 100);
            cell.style.backgroundColor = ''; // Reset cell color
        }
    }
}

function highlightCell(cell) {
    const cellValue = parseInt(cell.textContent);
    if (cellValue % 2 === 0) {
        cell.style.backgroundColor = 'lightblue';
    } else {
        cell.style.backgroundColor = 'lightgreen';
    }
}

// Function to get the count of green (lightgreen) and blue (lightblue) cells in a row or column
function countGreenBlueInRowCol(table, row, col) {
    let count = 0;

    for (let i = 0; i < table.rows.length; i++) {
        if (i === row && (table.rows[i].cells[col].style.backgroundColor === 'lightgreen' || table.rows[i].cells[col].style.backgroundColor === 'lightblue')) {
            count++;
        }

        if (table.rows[i].cells[col].style.backgroundColor !== '') {
            if (i === row && (table.rows[i].cells[col].style.backgroundColor === 'lightgreen' || table.rows[i].cells[col].style.backgroundColor === 'lightblue')) {
                count++;
            }
        }
    }
    return count;
}

// Function to check if the cell can be selected based on constraints
function canSelectCell(table, row, col, n) {
    let selectedGreenBlue = 0;

    for (let i = 0; i < table.rows.length; i++) {
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            if ((i === row || j === col) && !(i === row && j === col)) {
                if (table.rows[i].cells[j].style.backgroundColor === 'lightgreen' || table.rows[i].cells[j].style.backgroundColor === 'lightblue') {
                    selectedGreenBlue++;
                    if ((i === row && Math.abs(j - col) <= 1) || (j === col && Math.abs(i - row) <= 1)) {
                        return false; // Neighbor in row or column
                    }
                }
            }
        }
    }

    return selectedGreenBlue < n;
}


// Function to handle cell selection based on constraints
function selectCellsInRowCol(table, row, col, n) {
    const currentCell = table.rows[row].cells[col];

    if ((currentCell.style.backgroundColor === 'lightgreen' || currentCell.style.backgroundColor === 'lightblue') && countGreenBlueInRowCol(table, row, col) >= n) {
        currentCell.style.backgroundColor = '';
    } else if (canSelectCell(table, row, col, n)) {
        if (currentCell.style.backgroundColor === 'yellow') {
            currentCell.style.backgroundColor = '';
        } else if (currentCell.style.backgroundColor === '') {
            if (currentCell.textContent % 2 === 0) {
                currentCell.style.backgroundColor = 'lightblue';
            } else {
                currentCell.style.backgroundColor = 'lightgreen';
            }
        }
    }
}


function transposeTable() {
    const table = document.getElementById('myTable');
    const cellColors = [];

    for (let i = 0; i < table.rows.length; i++) {
        cellColors.push([]);
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            cellColors[i][j] = table.rows[i].cells[j].style.backgroundColor;
        }
    }

    const newTable = [];
    for (let i = 0; i < table.rows.length; i++) {
        newTable.push([]);
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            newTable[i][j] = table.rows[j].cells[i].textContent;
        }
    }

    table.innerHTML = '';
    for (let i = 0; i < newTable.length; i++) {
        const row = table.insertRow();
        for (let j = 0; j < newTable[i].length; j++) {
            const cell = row.insertCell();
            cell.textContent = newTable[i][j];
            cell.style.backgroundColor = cellColors[j][i]; // Apply previous colors after transposing
        }
    }
}

function addRow() {
    const table = document.getElementById('myTable');
    const newRow = table.insertRow();

    for (let j = 0; j < table.rows[0].cells.length; j++) {
        const cell = newRow.insertCell();
        cell.textContent = getRandomInt(1, 100);
        cell.style.backgroundColor = ''; // Reset cell color
    }
}

function addColumn() {
    const table = document.getElementById('myTable');
    for (let i = 0; i < table.rows.length; i++) {
        const cell = table.rows[i].insertCell();
        cell.textContent = getRandomInt(1, 100);
        cell.style.backgroundColor = ''; // Reset cell color
    }
}

document.getElementById('myTable').addEventListener('click', function(event) {
    if (event.target.nodeName === 'TD') {
        const cell = event.target;
        const rowIndex = cell.parentNode.rowIndex;
        const cellIndex = cell.cellIndex;
        const maxCells = parseInt(document.getElementById('maxCells').value);
        selectCellsInRowCol(document.getElementById('myTable'), rowIndex, cellIndex, maxCells);
    }
});

function createNewTable() {
    const tableSize = parseInt(document.getElementById('tableSize').value);
    createTable(tableSize);
}

createNewTable(); // Создание таблицы при загрузке страницы