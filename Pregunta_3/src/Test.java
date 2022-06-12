import junit.framework.TestCase;

public class Test extends TestCase {
	
	public void testallocate() {
		Buddy_system buddy=new Buddy_system(128);
		buddy.allocate(32, "juan");
	    buddy.allocate(8, "luis");  
		assertTrue(buddy.mapper.containsKey("juan")==true);
		assertTrue(buddy.mapper.containsKey("luis")==true);
		assertTrue(buddy.hm.get(0)==32);
		assertTrue(buddy.hm.get(32)==8);
		buddy.allocate(8, "luis");
		assertTrue(buddy.mapper.size()==2);
	}
	public void testdeallocate() {
		Buddy_system buddy=new Buddy_system(128);
		buddy.allocate(32, "juan");
	    buddy.allocate(8, "luis");
		buddy.deallocate("juan");
		buddy.deallocate("luis");
		assertTrue(buddy.mapper.containsKey("juan")==false);
		assertTrue(buddy.mapper.containsKey("luis")==false);
		assertTrue(buddy.hm.size()==0);
	
		}
	public void testPrint() {
		Buddy_system buddy=new Buddy_system(128);
		buddy.allocate(32,"juan");
		buddy.PrintFreeAllocate();
		
	
		}
}
