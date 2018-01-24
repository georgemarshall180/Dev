package org.totalbeginner.tutorial;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class PersonTest {

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testPerson() {
		Person p1 = new Person();
		assertEquals(" unknown name", p1.getName());
		assertEquals(3, p1.getMaximumBooks());
	}

	@Test
	public void testSetName() {
		Person p2 = new	Person();
		p2.setName("Fred");
		assertEquals("Fred", p2.getName());
	}

	@Test
	public void testSetMaximumBooks() {
		Person p3 = new Person();
		p3.setMaximumBooks(10);
		assertEquals(10,p3.getMaximumBooks());
	}
	@Test
	public void testToString() {
		Person p4 = new Person();
		p4.setName("Fred Flintstone");
		p4.setMaximumBooks(7);
		String testString = "Fred Flintstone(7 books)";
		assertEquals(testString, p4.toString());
		
	}

}
