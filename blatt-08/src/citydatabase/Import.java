package citydatabase;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.nio.file.Paths;

/**
 * This Class holds all functions doing import stuff.
 */
public class Import {

	/**
	 * Reads DatabaseFile, parses each line and puts it into
	 * a field. Returns this field.
	 * @param databaseFile
	 * @throws Exception 
	 */
	public static Object[][] importDatabase(URL url) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
		
		// Next we need to count the lines to know how many cities
		// we have in our databaseFile (each line = one city)
		// We need this information to know how big our
		// field has to be.
		
		int countedLines = Utils.countLines(br);
		
		
		// We need to reset the BufferedReader
		br.close(); // Close it
		br = new BufferedReader(new InputStreamReader(url.openStream())); // init it again
		
		// Init cities
		// We will have countedLines (n) city entries, each city
		// has 5 different "columns".
		Object[][] cities = new Object[countedLines][5];
		
		importFromDatabaseFile(br, cities);

		br.close();
		
		// Now sort cities
		Utils.sortCitiesByName(cities);
		
		return cities;
	}
	
	public static Object[][] importDatabase(String databaseFile) throws Exception {
		return importDatabase(Paths.get(databaseFile).toUri().toURL());
	}
		
	/**
	 * This method will go through each line in BufferedReader
	 * and assign the parsedLine to the this.cities field.
	 * @param br
	 * @throws IOException
	 */
	public static void importFromDatabaseFile(BufferedReader br, Object[][] cities) throws IOException {
		int i = 0;
		String line = null;
		while ((line = br.readLine()) != null) {
			cities[i] = Utils.parseCitiesLine(line);
			i++;
		}
	}

}
