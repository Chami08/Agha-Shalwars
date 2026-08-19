// Hamburger Menu Toggle
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

if (hamburger) {
    hamburger.addEventListener('click', function() {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close menu when a link is clicked
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function() {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });
}



// ================================
// Admin Product Search & Filter
// ================================

function searchProducts() {
    filterProducts();
}


function filterProducts() {

    const searchInput =
        document.getElementById("productSearch");

    const categorySelect =
        document.getElementById("categoryFilter");

    // If these elements don't exist,
    // do nothing.
    if (!searchInput || !categorySelect) {
        return;
    }

    const search =
        searchInput.value.toLowerCase();

    const category =
        categorySelect.value;

    const products =
        document.querySelectorAll(".manage-product-item");


    products.forEach(function(product) {

        const name =
            product.getAttribute("data-name");

        const productCategory =
            product.getAttribute("data-category");


        const matchesSearch =
            name.includes(search);


        const matchesCategory =
            category === "all" ||
            productCategory === category;


        if (matchesSearch && matchesCategory) {

            product.style.display = "grid";

        } else {

            product.style.display = "none";

        }

    });

}


// ================================
// Delete Product Confirmation
// ================================

function confirmDelete() {

    return confirm(
        "Are you sure you want to delete this product?"
    );

}