'''Tests if graph structure is working as expected'''
from graph.graph import Graph


def keys(vertices):
    '''
        Gets vertices' keys.

        set_ (set): Set of vertices.
    '''
    return {v.key for v in vertices}


def test_neighbours():
    '''
        Tests if the graph is able to link and unlink vertices as neighbours.
    '''
    graph = Graph()
    graph.add('Olegário')
    graph.add('Tiz')
    graph.add('Amigo do tiz')

    assert len(graph.vertices) == 3

    graph.link('Tiz', 'Amigo do tiz')
    graph.link('Tiz', 'Olegário')


    # ------------------------------------------------------

    graph.unlink('Tiz', 'Amigo do tiz')
    graph.unlink('Amigo do tiz', 'Tiz')

    # ------------------------------------------------------

    assert set(graph.vertices) == {'Olegário', 'Tiz', 'Amigo do tiz'}
    assert keys(graph['Olegário'].neighbours) == {'Tiz'}
    assert keys(graph['Tiz'].neighbours) == {'Olegário'}
    assert graph.random_vertex() in graph.vertices.values()

    graph.remove('Amigo do tiz')

    assert graph.order() == 2


def test_regular():
    '''
        Tests if the graph is able to link and unlink vertices as neighbours.
    '''
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)

    graph.link(0, 1)
    graph.link(0, 2)

    assert not graph.regular()

    graph.link(1, 2)

    assert graph.regular()


def test_complete():
    '''
        Tests if the graph is able to recognize when it's complete or not.
    '''
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)
    graph.add(3)

    assert not graph.complete()

    graph.link(0, 1)

    assert not graph.complete()

    graph.link(0, 2)
    graph.link(0, 3)

    graph.link(1, 2)

    graph.link(2, 3)

    assert not graph.complete()

    graph.link(1, 3)

    assert graph.complete()


def test_transitive_closure():
    '''
        Tests if the graph is able to generate transitive closures correctly.
    '''
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)
    graph.add(3)
    graph.add(4)
    graph.add(5)

    assert keys(graph.transitive_closure(0)) == {0}

    graph.link(0, 1)

    assert keys(graph.transitive_closure(0)) == {0, 1}

    graph.link(2, 3)

    assert keys(graph.transitive_closure(2)) == {2, 3}

    graph.link(1, 2)

    assert keys(graph.transitive_closure(2)) == {0, 1, 2, 3}
    assert keys(graph.transitive_closure(5)) == {5}

    graph.link(4, 4)

    assert keys(graph.transitive_closure(4)) == {4}

    graph.link(4, 5)

    assert keys(graph.transitive_closure(4)) == {4, 5}


def test_connected():
    '''
        Tests if the graph is able to recognize when it's complete or not.
    '''
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)
    graph.add(3)
    graph.add(4)
    graph.add(5)

    assert not graph.connected()

    graph.link(0, 1)

    assert not graph.connected()

    graph.link(2, 3)
    graph.link(1, 2)
    graph.link(4, 4)
    graph.link(4, 5)

    assert not graph.connected()

    graph.link(0, 4)

    assert graph.connected()


def test_tree():
    '''
        Tests if the graph is able to recognize when it's a tree or not.
    '''
    graph = Graph()

    graph.add(0)
    graph.add(1)
    graph.add(2)
    graph.add(3)
    graph.add(4)
    graph.add(5)

    assert not graph.tree()

    graph.link(0, 1)
    graph.link(0, 2)
    graph.link(3, 4)
    graph.link(4, 5)

    assert not graph.tree()

    graph.link(0, 5)

    assert graph.tree()

    graph.link(2, 3)

    assert not graph.tree()

    graph.unlink(2, 3)
    graph.link(1, 2)

    assert not graph.tree()
