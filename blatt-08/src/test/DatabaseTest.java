package test;

import org.junit.Test;

import citydatabase.Database;
import static org.junit.Assert.*;

public class DatabaseTest {
	@Test
	public void testSearchFirstByPrefix1() throws Exception {
		Database db = new Database(
			this.getClass().getResource("testCities2.txt")
		);
				
		assertEquals(0, db.searchFirstByPrefix("buch haim"));
		assertEquals(1, db.searchFirstByPrefix("frei"));
		assertEquals(2, db.searchFirstByPrefix("freibu"));
		assertEquals(3, db.searchFirstByPrefix("freibur"));
		assertEquals(3, db.searchFirstByPrefix("freibur"));
		assertEquals(4, db.searchFirstByPrefix("t"));

	}
	
	/*@Test
	public void testSearchFirstByPrefixUTF8() throws Exception {
		Database db = new Database(
			this.getClass().getResource("testCities3.txt")
		);
				
		assertEquals(0, db.searchFirstByPrefix("å"));
		assertEquals(1, db.searchFirstByPrefix("ž"));
	}*/
	
	@Test
	public void testSearchByPrefixDescendingOrder() throws Exception {
		Database db = new Database(
				this.getClass().getResource("testCities2.txt")
		);
		
		Object[][] foundCities = db.searchByPrefix("Frei");
		assertEquals(3, foundCities.length);
		assertEquals("Freibuch", (String) foundCities[0][0]);
		assertEquals("Freiberg", (String) foundCities[1][0]);
		assertEquals("Freiburg", (String) foundCities[2][0]);
	}
}