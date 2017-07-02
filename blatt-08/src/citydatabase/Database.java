package citydatabase;

import java.net.URL;
import java.util.LinkedList;

/**
 * Database Class.
 * Reads Database File and you can perform Prefix
 * Searches on it.
 */
public class Database {

	public Object[][] cities;
	
	/**
	 * Import from string filepath (has to be local file).
	 * @param databaseFile
	 * @throws Exception
	 */
	public Database(String databaseFile) throws Exception {
		this.cities = Import.importDatabase(databaseFile);
	}
	
	/**
	 * Import from URL, can also be resource (for testing).
	 * @param url
	 * @throws Exception
	 */
	public Database(URL url) throws Exception {
		this.cities = Import.importDatabase(url);
	}
	
	/**
	 * Searches all Cities starting with prefix and returns
	 * them ordered by population (descending). Lower
	 * cases prefix, so it's not case sensitive.
	 * @param prefix
	 * @return
	 */
	public Object[][] searchByPrefix(String prefix) {
		prefix = prefix.toLowerCase();
		int first = searchFirstByPrefix(prefix);
		
		// Didn't find a first one, so stop here
		if (first == -1) {
			return null;
		}
		
		LinkedList<Object[]> found = new LinkedList<Object[]>();
		
		found.add(this.cities[first]);
		
		for (int i = first + 1; i < this.cities.length; i++) {
			String cityName = (String) this.cities[i][0];
			
			if (cityName.toLowerCase().startsWith(prefix)) {
				found.add(this.cities[i]);
			} else {
				break;
			}
		}
		
		Utils.sortByPopulation(found);
		return found.toArray(new Object[found.size()][5]);

	}
	
	/**
	 * This function searches the first city starting with
	 * prefix. It uses the binary search algorithm.
	 * prefix has to be lower cased!
	 * Returns -1 or index. -1 if not found.
	 * https://de.wikipedia.org/wiki/Bin%C3%A4re_Suche#C
	 * @param prefix
	 * @return
	 */
	public int searchFirstByPrefix(String prefix) {
		int lo = 0;
		int hi = this.cities.length - 1;
		int lastFound = -1;
		String cityName;
		boolean startsWith;
		while (lo <= hi) {
			// Calculate new mid
			int mid = lo + (hi - lo) / 2;

			cityName = ((String) this.cities[mid][0]).toLowerCase();
			startsWith = cityName.startsWith(prefix);
			
			//System.out.println(cityName + " " + startsWith + " " + prefix);
						
			// if we found a country, save it
			if (startsWith) {
				lastFound = mid;
			}		   
			
			int compareTo = cityName.compareTo(prefix);
			
			if (startsWith || compareTo > 0) {
				// we found one which matches,
				// look on the left side, maybe we will find
				// something matching even better.
				// Or compareTo > 0, also look on the left side
				hi = mid - 1;
			} else if (compareTo < 0) {
				// look on the right side
				lo = mid + 1;
			} else {
				// compareTo == 0, so it equals. We already found
				// the best matching, so don't waste time and stop
				// here
				break;
			}
		}
		return lastFound;
	}
}
