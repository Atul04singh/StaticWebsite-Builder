<!-- Update Instruction: delete option not working -->

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