package bot;

//@YEET PREMEBOT BETA (ONLY FOR SHIRTS/JACKETS/HOODIE/ANYTHING THAT GOES FOR SMALL/MEDIUM/LARGE)

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;



public class Preme{

	public static void main(String[] args) throws InterruptedException {
		for(int x = 0; x <= 10; x++){
		//Create Firefox driver to drive the browser
		WebDriver bot = new FirefoxDriver();
		WebDriverWait wait = new WebDriverWait(bot, 60);
		WebDriverWait drop = new WebDriverWait(bot, 1000000000);
		//COPY AND PASTE THE PREME LINK
		bot.get("http://google.com");
		//COPS THE PREME
		drop.until(ExpectedConditions.elementToBeClickable(By.id("size")));
		//MAKES SURE TO COP THE PREME IN YOUR SIZE
		new Select(bot.findElement(By.id("size"))).selectByVisibleText("Medium");
		Thread.sleep(2000);
		bot.findElement(By.name("commit")).click();
		Thread.sleep(500);
		
		
		//THE PART OF THE CODE IM UNSURE ABOUT SUPREME IS WEIRD
		new Select(bot.findElement(By.id("cart"))).selectByVisibleText("checkout now");
		//THE PART OF THE CODE IM UNSURE ABOUT SUPREME IS WEIRD
		
		//needs to be tested but pretty sure it should all work
		wait.until(ExpectedConditions.elementToBeClickable(By.id("order_billing_name")));
		bot.findElement(By.id("order_billing_name")).sendKeys("Juan Jimenez");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("order_email")));
		bot.findElement(By.id("order_email")).sendKeys("EMAIL GOES HERE");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("order_tel")));
		bot.findElement(By.id("order_tel")).sendKeys("PHONE NUMBER GOES HERE");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("bo")));
		bot.findElement(By.id("bo")).sendKeys("ADRESS GOES HERE");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("oba3")));
		bot.findElement(By.id("oba3")).sendKeys("BILLING ADRESS 2 GOES HERE");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("order_billing_zip")));
		bot.findElement(By.id("order_billing_zip")).sendKeys("ZIP CODE GOES HERE");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("order_billing_city")));
		bot.findElement(By.id("order_billing_city")).sendKeys("CITY GOES HERE");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("order_billing_state")));
		new Select(bot.findElement(By.id("order_billing_state"))).selectByVisibleText("NY");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("order_billing_country")));
		new Select(bot.findElement(By.id("order_billing_country"))).selectByVisibleText("USA");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("credit_card_type")));
		new Select(bot.findElement(By.id("credit_card_type"))).selectByVisibleText("Visa / American Express / Mastercard ");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("cnb")));
		bot.findElement(By.id("cnb")).sendKeys("CARD NUMBER GOES HERE");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("credit_card_month")));
		new Select(bot.findElement(By.id("credit_card_type"))).selectByVisibleText("01/02/03/04/05/06/07/08/09/10/11/12");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("credit_card_year")));
		new Select(bot.findElement(By.id("credit_card_type"))).selectByVisibleText("2016/2017/2018...2026");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("vval")));
		bot.findElement(By.id("vval")).sendKeys("CCV FOR CREDIT CARD GOES HERE");
		wait.until(ExpectedConditions.elementToBeClickable(By.id("order_terms")));
		bot.findElement(By.id("order_terms")).click();
		wait.until(ExpectedConditions.elementToBeClickable(By.name("commit")));
		bot.findElement(By.name("commit")).click();
		}
	}
}
