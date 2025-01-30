package com.victorgarciarubio.ecommerce;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class SeleniumTests {

    private WebDriver driver;
    private WebDriverWait wait;

    @BeforeEach
    public void setUp() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless"); // Run in headless mode (optional)
        driver = new ChromeDriver(options);
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @AfterEach
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    public void testEcommerceApplication() {
        // Navigate to the application
        driver.get("http://localhost:3000");

        // Test 1: Check if the page title is correct
        assertEquals("E-commerce Application", driver.getTitle(), "Page title is incorrect");

        // Test 2: Check if the product list is loaded
        WebElement productList = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".product-list")));
        assertTrue(productList.isDisplayed(), "Product list is not displayed");

        // Test 3: Search for a product
        WebElement searchInput = driver.findElement(By.id("search-input"));
        searchInput.sendKeys("laptop");
        searchInput.submit();
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".search-results")));
        List<WebElement> searchResults = driver.findElements(By.cssSelector(".product-item"));
        assertTrue(searchResults.size() > 0, "No search results found");

        // Test 4: Add a product to the cart
        WebElement addToCartButton = driver.findElement(By.cssSelector(".add-to-cart-button"));
        addToCartButton.click();
        WebElement cartCount = driver.findElement(By.cssSelector(".cart-count"));
        assertEquals("1", cartCount.getText(), "Product not added to cart");

        // Test 5: Navigate to the cart page
        WebElement cartLink = driver.findElement(By.cssSelector(".cart-link"));
        cartLink.click();
        WebElement cartPage = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".cart-page")));
        assertTrue(cartPage.isDisplayed(), "Cart page is not displayed");
    }
}