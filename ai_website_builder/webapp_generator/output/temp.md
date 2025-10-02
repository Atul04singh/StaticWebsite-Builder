```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>To-Do List</h1>
        <div class="input-area">
            <input type="text" id="itemInput" placeholder="Add new item">
            <button id="addItemBtn">Add</button>
        </div>
        <ul id="todoList">
        </ul>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
body {
    font-family: sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: 20px auto;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    overflow: hidden;
}

h1 {
    text-align: center;
    padding: 20px;
    background-color: #3498db;
    color: white;
    border-radius: 8px;
}

.input-area {
    display: flex;
    margin: 10px;
}

.input-area input[type="text"] {
    width: 80%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-right: 10px;
}

.input-area button {
    background-color: #2ecc71;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

#todoList {
    list-style: none;
    padding: 0;
    margin: 0;
}

#todoList li {
    background-color: #fff;
    padding: 10px;
    border: 1px solid #ddd;
    margin-bottom: 5px;
    border-radius: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#todoList li button {
    background-color: #e74c3c;
    color: white;
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

#todoList li.completed {
    text-decoration: line-through;
    color: #95a5a6;
}
```

```javascript
const itemInput = document.getElementById('itemInput');
const addItemBtn = document.getElementById('addItemBtn');
const todoList = document.getElementById('todoList');

// Function to add a new item to the to-do list
function addItem() {
    const itemText = itemInput.value.trim();

    if (itemText !== '') {
        const li = document.createElement('li');
        li.textContent = itemText;
        li.classList.add('completed'); // Add completed class for styling
        li.innerHTML = `<button class="deleteItemBtn">Delete</button>`;
        todoList.appendChild(li);
        itemInput.value = '';
    }
}

// Function to delete an item from the to-do list
function deleteItem(event) {
    event.preventDefault();
    const btn = event.target;
    const li = btn.parentNode;
    todoList.removeChild(li);
}

// Add event listener to the add button
addItemBtn.addEventListener('click', addItem);

// Add event listener to the delete buttons
const deleteBtns = document.querySelectorAll('.deleteItemBtn');
deleteBtns.forEach(btn => {
    btn.addEventListener('click', deleteItem);
});
```
