package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;

import org.junit.Test;

import citydatabase.Utils;
import org.junit.Assert;


public class UtilsTest {

	@Test
	public void testCountLines1() throws IOException {
		InputStream pathTestFile1 = this.getClass().getResourceAsStream("testFile1.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(pathTestFile1));
	    
		Assert.assertEquals(Utils.countLines(br), 9);
	}
	
	@Test
	public void testParseCitiesLine() {
		Object[] expectedCityObject = new Object[5];
		expectedCityObject[0] = "Buchhaim";
		expectedCityObject[1] = "Zamonien";
		expectedCityObject[2] = 22000;
		expectedCityObject[3] = new Float(42.0012);
		expectedCityObject[4] = new Float(13.0372);

		
		Object[] parsedCityObject = Utils.parseCitiesLine("Buchhaim\tZamonien\t22000\t42.0012\t13.0372");
		
		Assert.assertArrayEquals(expectedCityObject, parsedCityObject);
	}

	@Test
	public void testParseCitiesLineWithWhitespace() {
		Object[] expectedCityObject = new Object[5];
		expectedCityObject[0] = "Buch haim";
		expectedCityObject[1] = "Zamonien";
		expectedCityObject[2] = 22000;
		expectedCityObject[3] = new Float(42.0012);
		expectedCityObject[4] = new Float(13.0372);
		
		Object[] parsedCityObject = Utils.parseCitiesLine("Buch haim\tZamonien\t22000\t42.0012\t13.0372");
		
		Assert.assertArrayEquals(expectedCityObject, parsedCityObject);
	}
	
	/*@Test
	public void testParseCitiesLineWithUTF8() {
		Object[] expectedCityObject = new Object[5];
		expectedCityObject[0] = "Zybiszów";
		expectedCityObject[1] = "Zamonien";
		expectedCityObject[2] = 22000;
		expectedCityObject[3] = new Float(42.0012);
		expectedCityObject[4] = new Float(13.0372);

		
		Object[] parsedCityObject = Utils.parseCitiesLine("Zybiszów\tZamonien\t22000\t42.0012\t13.0372");
		
		Assert.assertArrayEquals(expectedCityObject, parsedCityObject);
	}*/
	
	@Test
	public void testSortByPopulation1() {
		LinkedList<Object[]> cities = new LinkedList<Object[]>();
		cities.add(
			new Object[]{"BuchHaim", "Zamonien", 5, new Float(13.0), new Float(14.0)}
		);
		cities.add(
			new Object[]{"Freiburg", "Germany", 1, new Float(52.0), new Float(11.0)}
		);
		cities.add(
			new Object[]{"TestCity", "TestCountry", 3, new Float(100.0), new Float(420.0)}
		);
		
		Utils.sortByPopulation(cities);

		Assert.assertArrayEquals(
				new Object[]{"TestCity", "TestCountry", 3, new Float(100.0), new Float(420.0)},
			cities.get(1)
		);

		Assert.assertArrayEquals(
			new Object[]{"Freiburg", "Germany", 1, new Float(52.0), new Float(11.0)},
			cities.get(2)
		);
	}
	
	@Test
	public void testSortCitiesByName() {
		Object[][] cities = new Object[][]{
				new Object[]{"Ubersee"},
				new Object[]{"Übersee"},
				new Object[]{"Úbeda"},
				new Object[]{"Uberlândia"},
				new Object[]{"Übersee"},
				new Object[]{"Ćmielów"}
		};
		
		Utils.sortCitiesByName(cities);
		
		Assert.assertArrayEquals(
			new Object[][]{
					new Object[]{"Uberlândia"},
					new Object[]{"Ubersee"},
					new Object[]{"Úbeda"},
					new Object[]{"Übersee"},
					new Object[]{"Übersee"},
					new Object[]{"Ćmielów"}
			}, 
			cities
		);
	}

}
