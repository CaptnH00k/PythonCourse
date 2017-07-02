package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

import org.junit.Assert;
import org.junit.Test;

import citydatabase.Import;

public class ImportTest {

	@Test
	public void testImportFromDatabaseFile1() throws IOException {
		InputStream pathTestFile1 = this.getClass().getResourceAsStream("testCities1.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(pathTestFile1));
		
		Object[][] cities = new Object[2][5];
		
		Import.importFromDatabaseFile(br, cities);
		
		Object[][] expectedCities = new Object[][] {
			{"Buch Haim", "Zamonien", 22000, new Float(42.00312), new Float(13.00137)},
			{"TestCity", "TestCountry", 13, new Float(12.000), new Float(14.000)}
		};
		
		Assert.assertArrayEquals(expectedCities, cities);
	}
	
	@Test
	public void testImportDatabase() throws Exception {
		Object[][] importedCities = Import.importDatabase(
			this.getClass().getResource("testCities1.txt")
		);
		
		Object[][] expectedCities = new Object[][] {
			{"Buch Haim", "Zamonien", 22000, new Float(42.00312), new Float(13.00137)},
			{"TestCity", "TestCountry", 13, new Float(12.000), new Float(14.000)}
		};
		
		Assert.assertArrayEquals(expectedCities, importedCities);
	}

	/*@Test
	public void testImportDatabaseUTF8() throws Exception {
		Object[][] importedCities = Import.importDatabase(
			this.getClass().getResource("testCities3.txt")
		);
		
		Object[][] expectedCities = new Object[][] {
			{"ÅŽybiszów", "Norway", 1162, new Float(63.967222), new Float(10.218611)},
			{"Žytkavičy", "Belarus", 16600, new Float(52.233333), new Float(27.866667)}
		};

		Assert.assertArrayEquals(expectedCities, importedCities);
	}*/

}
