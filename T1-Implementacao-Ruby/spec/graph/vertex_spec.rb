require 'vertex'

describe Vertex, type: 'graph' do
  subject(:subject) { Vertex.new(nil) }

  before (:each) do
    subject.neighbours.clear
    @vertex = Vertex.new(nil)
    @vertex.neighbours.clear
    @other_vertex = Vertex.new(1)
    @other_vertex.neighbours.clear
  end

  it '#degree' do
    expect(subject.degree).to eq(0)
  end

  it '#are_neighbours' do
    expect(subject.are_neighbours?(@vertex)).to be_falsy
  end

  it '#has_neighbours?' do
    expect(subject.has_neighbours?).to be_falsy
  end

  it '#check_data' do
    expect(@other_vertex.check_data(1)).to be_truthy
  end

  it 'no set method for data' do
    expect{subject.data = 2}.to raise_error(NoMethodError)
  end
end
