require 'graph'

describe Graph, type: 'graph' do
  before(:each) do
    subject.vertices.clear
    @vertex = Vertex.new(nil)
    @other_vertex = Vertex.new(nil)
    @final_vertex = Vertex.new(nil)
  end

  it '#add_vertex' do
    subject.add_vertex(@vertex)
    expect(subject.vertices.size).to eq(1)
  end

  it '#connect_vertices' do
    subject.add_vertex(@vertex)
    subject.add_vertex(@other_vertex)
    subject.connect_vertices(@vertex, @other_vertex)
    expect(@vertex.degree).to eq(1)
  end

  it '#disconnect_vertices' do
    subject.add_vertex(@vertex)
    subject.add_vertex(@other_vertex)
    subject.connect_vertices(@vertex, @other_vertex)
    subject.disconnect_vertices(@other_vertex, @vertex)
    expect(@vertex.degree).to eq(0)
  end

  it '#disconnect_all_vertices' do
    subject.add_vertex(@vertex)
    subject.add_vertex(@other_vertex)
    subject.add_vertex(@final_vertex)
    subject.connect_vertices(@vertex, @other_vertex)
    subject.connect_vertices(@vertex, @final_vertex)
    subject.disconnect_all_vertices(@vertex)
    expect(@vertex.degree).to eq(0)
  end

  it '#remove_vertex' do
    subject.add_vertex(@vertex)
    subject.remove_vertex(@vertex)
    expect(subject.vertices.size).to eq(0)
  end

  it '#order' do
    expect(subject.order).to eq(0)
  end

  it '#depth_first_search' do
    #
    #          1
    #         / \
    #        2   3
    #       / \ / \
    #      4  5 6 7
    vertex_1 = Vertex.new(1)
    vertex_2 = Vertex.new(2)
    vertex_3 = Vertex.new(3)
    vertex_4 = Vertex.new(4)
    vertex_5 = Vertex.new(5)
    vertex_6 = Vertex.new(6)
    vertex_7 = Vertex.new(7)
    subject.add_vertex(vertex_1)
    subject.add_vertex(vertex_2)
    subject.add_vertex(vertex_3)
    subject.add_vertex(vertex_4)
    subject.add_vertex(vertex_5)
    subject.add_vertex(vertex_6)
    subject.add_vertex(vertex_7)
    subject.connect_vertices(vertex_1, vertex_2)
    subject.connect_vertices(vertex_1, vertex_3)
    subject.connect_vertices(vertex_2, vertex_4)
    subject.connect_vertices(vertex_2, vertex_5)
    subject.connect_vertices(vertex_3, vertex_6)
    subject.connect_vertices(vertex_3, vertex_7)
    v = subject.depth_first_search(subject.select_random_vertex, Set.new, 3)
    expect(v.data).to eq(3)
  end
end
